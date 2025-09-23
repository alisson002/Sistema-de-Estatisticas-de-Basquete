# cronometro_basquete/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-sua-chave-secreta-aqui'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'timer_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cronometro_basquete.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cronometro_basquete.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# cronometro_basquete/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timer_app.urls')),
]

# timer_app/urls.py
from django.urls import path
from .paginas import views

app_name = 'timer_app'

urlpatterns = [
    path('', views.timer_view, name='timer'),
    path('api/timer-state/', views.get_timer_state, name='get_timer_state'),
    path('api/update-timer/', views.update_timer, name='update_timer'),
]

# timer_app/models.py
from django.db import models
from django.utils import timezone

class TimerSession(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    time_remaining = models.IntegerField(default=0)  # em centésimos de segundo
    is_running = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Session {self.session_key} - {self.time_remaining/100:.2f}s"
    
    class Meta:
        verbose_name = "Sessão do Cronômetro"
        verbose_name_plural = "Sessões do Cronômetro"

# timer_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.views.decorators.http import require_http_methods
import json
from .models import TimerSession

def timer_view(request):
    """View principal do cronômetro"""
    # Garantir que há uma sessão ativa
    if not request.session.session_key:
        request.session.create()
    
    # Criar ou obter sessão do cronômetro
    timer_session, created = TimerSession.objects.get_or_create(
        session_key=request.session.session_key,
        defaults={
            'time_remaining': 0,
            'is_running': False
        }
    )
    
    context = {
        'timer_session': timer_session,
        'initial_time': timer_session.time_remaining,
        'is_running': timer_session.is_running,
    }
    
    return render(request, 'timer_app/timer.html', context)

def get_timer_state(request):
    """API para obter o estado atual do cronômetro"""
    if not request.session.session_key:
        return JsonResponse({'error': 'Sessão não encontrada'}, status=400)
    
    try:
        timer_session = TimerSession.objects.get(
            session_key=request.session.session_key
        )
        
        # Calcular tempo atual se estiver rodando
        if timer_session.is_running:
            time_elapsed = (timezone.now() - timer_session.last_updated).total_seconds()
            centiseconds_elapsed = int(time_elapsed * 100)
            current_time = max(0, timer_session.time_remaining - centiseconds_elapsed)
            
            # Atualizar no banco se necessário
            if current_time != timer_session.time_remaining:
                timer_session.time_remaining = current_time
                if current_time <= 0:
                    timer_session.is_running = False
                timer_session.save()
        else:
            current_time = timer_session.time_remaining
        
        return JsonResponse({
            'time_remaining': current_time,
            'is_running': timer_session.is_running,
            'formatted_time': f"{current_time//100:02d}.{current_time%100:02d}"
        })
        
    except TimerSession.DoesNotExist:
        return JsonResponse({'error': 'Sessão do cronômetro não encontrada'}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def update_timer(request):
    """API para atualizar o estado do cronômetro"""
    if not request.session.session_key:
        return JsonResponse({'error': 'Sessão não encontrada'}, status=400)
    
    try:
        data = json.loads(request.body)
        action = data.get('action')
        value = data.get('value', 0)
        
        timer_session, created = TimerSession.objects.get_or_create(
            session_key=request.session.session_key,
            defaults={
                'time_remaining': 0,
                'is_running': False
            }
        )
        
        if action == 'set_time':
            timer_session.time_remaining = max(0, min(2400, value))  # Entre 0 e 24s
            timer_session.is_running = False
            
        elif action == 'add_time':
            timer_session.time_remaining = max(0, min(2400, timer_session.time_remaining + value))
            
        elif action == 'subtract_time':
            timer_session.time_remaining = max(0, timer_session.time_remaining - value)
            
        elif action == 'toggle_play_pause':
            if timer_session.time_remaining > 0:
                timer_session.is_running = not timer_session.is_running
            
        elif action == 'stop':
            timer_session.is_running = False
            
        timer_session.save()
        
        return JsonResponse({
            'success': True,
            'time_remaining': timer_session.time_remaining,
            'is_running': timer_session.is_running,
            'formatted_time': f"{timer_session.time_remaining//100:02d}.{timer_session.time_remaining%100:02d}"
        })
        
    except (json.JSONDecodeError, TimerSession.DoesNotExist) as e:
        return JsonResponse({'error': str(e)}, status=400)

# timer_app/admin.py
from django.contrib import admin
from .models import TimerSession

@admin.register(TimerSession)
class TimerSessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'formatted_time', 'is_running', 'last_updated', 'created_at']
    list_filter = ['is_running', 'created_at', 'last_updated']
    search_fields = ['session_key']
    readonly_fields = ['created_at', 'last_updated']
    
    def formatted_time(self, obj):
        return f"{obj.time_remaining//100:02d}.{obj.time_remaining%100:02d}s"
    formatted_time.short_description = 'Tempo Restante'

# timer_app/apps.py
from django.apps import AppConfig

class TimerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'timer_app'
    verbose_name = 'Cronômetro de Basquete'