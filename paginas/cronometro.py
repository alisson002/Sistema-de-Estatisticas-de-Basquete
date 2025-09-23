import streamlit as st
import streamlit as st
import streamlit.components.v1 as components

def main():
    # Configurar página para tela cheia
    st.set_page_config(
        layout="wide",
    )
    
    # Esconder elementos do Streamlit para tela cheia
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    header {
        visibility: visible;
        height: 30px;
    }
    .stDeployButton {visibility: visible;}
    .stDecoration {visibility: hidden;}
    .st-emotion-cache-gf1xsr {visibility: hidden;}
    .st-emotion-cache-arp25b {visibility: hidden;}
    
    /* Remover padding e margin */
    .css-1d391kg {padding: 0rem 0rem 0rem;}
    .css-1rs6os {background-color: transparent;}
    .css-17eq0hr {background-color: transparent;}
    
    /* Forçar fundo escuro em toda a aplicação */
    .stApp {
        background: linear-gradient(135deg, #0e1117, #0e1117) !important;
        overflow: hidden !important;
        height: 100vh !important;
        position: fixed !important;
        width: 100vw !important;
        top: 0 !important;
        left: 0 !important;
    }
    
    .main .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
        height: 100vh !important;
        overflow: hidden !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
    }
    
    /* Sobrescrever qualquer fundo branco */
    .stApp > div, 
    .stApp > div > div,
    .main,
    .block-container {
        background: transparent !important;
        overflow: hidden !important;
    }
    
    /* Remover margens e espaçamentos */
    .main {
        padding: 0 !important;
        height: 100vh !important;
        overflow: hidden !important;
        position: fixed !important;
        width: 100vw !important;
        top: 0 !important;
        left: 0 !important;
    }
    
    /* Para versões mais novas do Streamlit */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0e1117, #0e1117) !important;
        overflow: hidden !important;
        height: 100vh !important;
        position: fixed !important;
        width: 100vw !important;
        top: 0 !important;
        left: 0 !important;
    }
    
    [data-testid="stMain"] {
        background: transparent !important;
        overflow: hidden !important;
        height: 100vh !important;
        position: fixed !important;
        width: 100vw !important;
        top: 0 !important;
        left: 0 !important;
    }
    
    [data-testid="block-container"] {
        padding: 0rem !important;
        max-width: 100% !important;
        height: 100vh !important;
        overflow: hidden !important;
        position: fixed !important;
        width: 100vw !important;
        top: 0 !important;
        left: 0 !important;
    }
    
    /* Impedir scroll em qualquer elemento */
    html, body {
        overflow: hidden !important;
        height: 100vh !important;
        position: fixed !important;
        width: 100vw !important;
    }
    
    h1#inicio {
        margin: 0 !important;
        padding: 0 0 !important;
        line-height: 0 !important;
        font-size: 0 !important; /* Reduz o tamanho da fonte se necessário */
    }

    /* Ou direciona o container pai */
    h1#inicio .st-emotion-cache-gf1xsr {
        margin: 0 !important;
        padding: 0 0 !important;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # HTML com React compilado (usando CDN)
    html_code = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <title>Cronômetro de Basquete - Django</title>
        
        <!-- Bootstrap CSS para responsividade extra -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
        
        <style>
            :root {
                --primary-green: #4ade80;
                --primary-yellow: #fbbf24;
                --primary-red: #ef4444;
                --bg-dark: #0e1117;
                --bg-darker: #030712;
                --text-gray: #9ca3af;
                --shadow-color: rgba(0, 0, 0, 0.4);
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html, body {
                height: 100vh;
                width: 100vw;
                background: linear-gradient(135deg, var(--bg-dark), var(--bg-dark));
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                overflow-x: hidden;
                position: relative;
                margin-top: -135px;
            }

            .main-container {
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 10vh;
                padding: 1rem;
            }

            .timer-wrapper {
                width: 100%;
                max-width: 400px;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 1.5rem;
            }

            /* Display do cronômetro */
            .timer-display {
                background: var(--bg-darker);
                border-radius: clamp(1rem, 3vw, 2rem);
                border: 4px solid var(--primary-green);
                width: 100%;
                aspect-ratio: 16/9;
                min-height: 150px;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 
                    0 8px 32px var(--shadow-color),
                    0 0 20px rgba(74, 222, 128, 0.2);
                transition: all 0.3s ease;
                position: relative;
            }

            .timer-display.border-green {
                border-color: var(--primary-green);
                box-shadow: 
                    0 8px 32px var(--shadow-color),
                    0 0 20px rgba(74, 222, 128, 0.2);
            }

            .timer-display.border-yellow {
                border-color: var(--primary-yellow);
                box-shadow: 
                    0 8px 32px var(--shadow-color),
                    0 0 30px rgba(251, 191, 36, 0.4);
            }

            .timer-display.border-red {
                border-color: var(--primary-red);
                box-shadow: 
                    0 8px 32px var(--shadow-color),
                    0 0 40px rgba(239, 68, 68, 0.6);
            }

            .timer-text {
                font-size: clamp(5rem, 12vw, 6rem);
                font-weight: 900;
                font-family: 'Courier New', monospace;
                letter-spacing: 0.1em;
                transition: color 0.3s ease;
                text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            }

            .timer-green { color: var(--primary-green); }
            .timer-yellow { color: var(--primary-yellow); }
            .timer-red { color: var(--primary-red); }

            /* Botões */
            .btn-custom {
                border: none;
                border-radius: 50%;
                font-weight: bold;
                box-shadow: 0 4px 15px var(--shadow-color);
                transition: all 0.2s ease;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #ffffff;
                color: #000;
                font-family: 'Segoe UI', sans-serif;
                user-select: none;
                -webkit-tap-highlight-color: transparent;
            }

            .btn-custom:hover:not(:disabled) {
                transform: scale(1.05);
                background: #ea580c;
                color: white;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
            }

            .btn-custom:active {
                transform: scale(0.95);
            }

            .btn-custom:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }

            .btn-large {
                width: clamp(60px, 15vw, 80px);
                height: clamp(60px, 15vw, 80px);
                font-size: clamp(0.8rem, 3vw, 1rem);
            }

            .btn-play {
                width: clamp(80px, 20vw, 100px);
                height: clamp(80px, 20vw, 100px);
                font-size: clamp(1rem, 4vw, 1.2rem);
                background: #ffffff;
                color: #000;
                margin: 0.8rem 0;
            }

            .btn-small {
                width: clamp(50px, 12vw, 65px);
                height: clamp(50px, 12vw, 65px);
                font-size: clamp(0.7rem, 2.5vw, 0.9rem);
            }

            .button-row {
                display: flex;
                gap: clamp(1.5rem, 5vw, 2.5rem);
                justify-content: center;
                width: 100%;
                margin-bottom: 0.5rem;
            }

            .button-row-small {
                display: flex;
                gap: clamp(0.8rem, 3vw, 1.5rem);
                justify-content: center;
                width: 100%;
                flex-wrap: wrap;
                margin-bottom: 0.8rem;
            }

            .status-text {
                text-align: center;
                color: var(--text-gray);
                font-size: clamp(0.8rem, 3vw, 1rem);
                font-weight: 500;
            }

            .play-icon, .pause-icon {
                width: clamp(20px, 6vw, 32px);
                height: clamp(20px, 6vw, 32px);
                pointer-events: none;
            }

            .play-icon {
                margin-left: 2px;
            }

            /* Loading indicator */
            .loading-indicator {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: var(--text-gray);
                font-size: 0.9rem;
            }

            /* Responsividade específica para dispositivos */
            
            /* Smartphones em modo retrato */
            @media (max-width: 576px) and (orientation: portrait) {
                .main-container {
                    padding: 0.5rem;
                }
                
                .timer-wrapper {
                    max-width: 100%;
                    gap: 1rem;
                }
                
                .timer-display {
                    min-height: 120px;
                    aspect-ratio: 2/1;
                }
                
                .button-row {
                    gap: 1.8rem;
                    margin-bottom: 0.8rem;
                }
                
                .button-row-small {
                    flex-wrap: wrap;
                    gap: 0.8rem;
                    margin-bottom: 1rem;
                }
                
                .btn-small {
                    min-width: 45px;
                    min-height: 45px;
                }
            }

            /* Smartphones em modo paisagem */
            @media (max-width: 896px) and (orientation: landscape) {
                .main-container {
                    padding: 0.5rem;
                    align-items: stretch;
                }
                
                .timer-wrapper {
                    max-width: 100%;
                    flex-direction: row;
                    align-items: center;
                    gap: 1rem;
                }
                
                .timer-display {
                    flex: 1;
                    max-width: 40%;
                    aspect-ratio: 3/2;
                }
                
                .controls-section {
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    gap: 0.5rem;
                    max-width: 60%;
                }
                
                .button-row, .button-row-small {
                    gap: 0.5rem;
                }
            }

            /* Tablets */
            @media (min-width: 577px) and (max-width: 1024px) {
                .timer-wrapper {
                    max-width: 500px;
                    gap: 2rem;
                }
                
                .timer-display {
                    min-height: 200px;
                }
            }

            /* Desktops grandes */
            @media (min-width: 1200px) {
                .timer-wrapper {
                    max-width: 600px;
                    gap: 2.5rem;
                }
                
                .timer-display {
                    min-height: 250px;
                }
            }

            /* Telas muito altas (modo retrato em desktop) */
            @media (min-height: 900px) and (orientation: portrait) {
                .timer-wrapper {
                    gap: 3rem;
                }
                
                .timer-display {
                    min-height: 300px;
                }
            }

            /* Ajustes para telas pequenas em altura */
            @media (max-height: 600px) {
                .main-container {
                    min-height: auto;
                    padding: 0.5rem;
                }
                
                .timer-wrapper {
                    gap: 0.8rem;
                }
                
                .timer-display {
                    min-height: 80px;
                    aspect-ratio: 3/1;
                }
            }

            /* Reduced motion */
            @media (prefers-reduced-motion: reduce) {
                .timer-display,
                .btn-custom,
                .timer-text {
                    transition: none;
                }
            }

            /* High contrast mode */
            @media (prefers-contrast: high) {
                .timer-display {
                    border-width: 6px;
                }
                
                .btn-custom {
                    border: 2px solid #000;
                }
            }

            /* Print styles */
            @media print {
                .main-container {
                    background: white;
                    color: black;
                }
                
                .btn-custom {
                    display: none;
                }
            }
        </style>
    </head>
    <body>
        <div class="main-container">
            <div class="timer-wrapper">
                <!-- Display do cronômetro -->
                <div id="timerDisplay" class="timer-display border-green">
                    <div id="timer" class="timer-text timer-green">00.00</div>
                    <div id="loadingIndicator" class="loading-indicator d-none">
                        Conectando...
                    </div>
                </div>

                <div class="controls-section">
                    <!-- Botões superiores: +24s e +14s -->
                    <div class="button-row">
                        <button class="btn-custom btn-large" onclick="setTime(24)" aria-label="Iniciar 24 segundos">
                            +24s
                        </button>
                        <button class="btn-custom btn-large" onclick="setTime(14)" aria-label="Iniciar 14 segundos">
                            +14s
                        </button>
                    </div>

                    <!-- Botão central: Play/Pause -->
                    <div class="button-row">
                        <button id="playPauseBtn" class="btn-custom btn-play" onclick="togglePlayPause()" disabled aria-label="Play/Pause">
                            <svg class="play-icon" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M8 5v14l11-7z"/>
                            </svg>
                        </button>
                    </div>

                    <!-- Botões de ajuste fino: +1s, +0.1s, +0.01s -->
                    <div class="button-row-small">
                        <button class="btn-custom btn-small" onclick="addTime(1)" aria-label="Adicionar 1 segundo">
                            +1s
                        </button>
                        <button class="btn-custom btn-small" onclick="addTime(0.1)" aria-label="Adicionar 0.1 segundo">
                            +0.1s
                        </button>
                        <button class="btn-custom btn-small" onclick="addTime(0.01)" aria-label="Adicionar 0.01 segundo">
                            +0.01s
                        </button>
                    </div>

                    <!-- Botões de subtração: -1s, -0.1s, -0.01s -->
                    <div class="button-row-small">
                        <button class="btn-custom btn-small" onclick="subtractTime(1)" aria-label="Subtrair 1 segundo">
                            -1s
                        </button>
                        <button class="btn-custom btn-small" onclick="subtractTime(0.1)" aria-label="Subtrair 0.1 segundo">
                            -0.1s
                        </button>
                        <button class="btn-custom btn-small" onclick="subtractTime(0.01)" aria-label="Subtrair 0.01 segundo">
                            -0.01s
                        </button>
                    </div>

                    <!-- Indicador de status -->
                    <div id="status" class="status-text">
                        Pressione +24s ou +14s para começar
                    </div>
                </div>
            </div>
        </div>

        <!-- Bootstrap JS para funcionalidades extras -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>

        <script>
            class BasketballTimer {
                constructor() {
                    this.time = 0;
                    this.isRunning = false;
                    this.intervalId = null;
                    this.updateInterval = null;
                    this.isOnline = navigator.onLine;
                    
                    // Elementos DOM
                    this.timerElement = document.getElementById('timer');
                    this.timerDisplayElement = document.getElementById('timerDisplay');
                    this.playPauseBtn = document.getElementById('playPauseBtn');
                    this.statusElement = document.getElementById('status');
                    this.loadingIndicator = document.getElementById('loadingIndicator');
                    
                    // Ícones SVG
                    this.playIcon = `
                        <svg class="play-icon" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M8 5v14l11-7z"/>
                        </svg>
                    `;
                    
                    this.pauseIcon = `
                        <svg class="pause-icon" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
                        </svg>
                    `;
                    
                    // CSRF Token para requisições Django
                    this.csrfToken = this.getCSRFToken();
                    
                    // Inicializar
                    this.init();
                    this.setupEventListeners();
                }
                
                getCSRFToken() {
                    const cookies = document.cookie.split(';');
                    for (let cookie of cookies) {
                        const [name, value] = cookie.trim().split('=');
                        if (name === 'csrftoken') {
                            return value;
                        }
                    }
                    return '';
                }
                
                async init() {
                    try {
                        this.showLoading(true);
                        await this.fetchTimerState();
                        this.startPeriodicUpdate();
                        this.showLoading(false);
                    } catch (error) {
                        console.error('Erro ao inicializar:', error);
                        this.handleOfflineMode();
                    }
                }
                
                setupEventListeners() {
                    // Listeners para conectividade
                    window.addEventListener('online', () => {
                        this.isOnline = true;
                        this.init();
                    });
                    
                    window.addEventListener('offline', () => {
                        this.isOnline = false;
                        this.handleOfflineMode();
                    });
                    
                    // Cleanup ao fechar
                    window.addEventListener('beforeunload', () => {
                        this.cleanup();
                    });
                    
                    // Listener para orientação da tela
                    window.addEventListener('orientationchange', () => {
                        setTimeout(() => this.updateDisplay(), 300);
                    });
                    
                    // Listener para redimensionamento
                    window.addEventListener('resize', () => {
                        this.updateDisplay();
                    });
                    
                    // Suporte a teclado
                    document.addEventListener('keydown', (event) => {
                        this.handleKeyboard(event);
                    });
                }
                
                handleKeyboard(event) {
                    if (event.target.tagName === 'INPUT') return;
                    
                    switch(event.code) {
                        case 'Space':
                            event.preventDefault();
                            this.togglePlayPause();
                            break;
                        case 'Digit1':
                            this.setTime(24);
                            break;
                        case 'Digit2':
                            this.setTime(14);
                            break;
                        case 'KeyR':
                            this.resetTimer();
                            break;
                    }
                }
                
                showLoading(show) {
                    if (show) {
                        this.loadingIndicator.classList.remove('d-none');
                        this.timerElement.style.opacity = '0.5';
                    } else {
                        this.loadingIndicator.classList.add('d-none');
                        this.timerElement.style.opacity = '1';
                    }
                }
                
                async fetchTimerState() {
                    if (!this.isOnline) return;
                    
                    try {
                        const response = await fetch('/api/timer-state/');
                        const data = await response.json();
                        
                        if (data.error) {
                            throw new Error(data.error);
                        }
                        
                        this.time = data.time_remaining;
                        this.isRunning = data.is_running;
                        this.updateDisplay();
                        
                    } catch (error) {
                        console.error('Erro ao buscar estado:', error);
                        this.handleOfflineMode();
                    }
                }
                
                async updateTimerOnServer(action, value = 0) {
                    if (!this.isOnline) {
                        this.handleLocalUpdate(action, value);
                        return;
                    }
                    
                    try {
                        const response = await fetch('/api/update-timer/', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': this.csrfToken,
                            },
                            body: JSON.stringify({
                                action: action,
                                value: value
                            })
                        });
                        
                        const data = await response.json();
                        
                        if (data.success) {
                            this.time = data.time_remaining;
                            this.isRunning = data.is_running;
                            this.updateDisplay();
                        } else {
                            throw new Error(data.error || 'Erro no servidor');
                        }
                        
                    } catch (error) {
                        console.error('Erro ao atualizar timer:', error);
                        this.handleLocalUpdate(action, value);
                    }
                }
                
                handleLocalUpdate(action, value) {
                    // Fallback para modo offline
                    switch(action) {
                        case 'set_time':
                            this.time = Math.max(0, Math.min(2400, value));
                            this.isRunning = false;
                            break;
                        case 'add_time':
                            this.time = Math.max(0, Math.min(2400, this.time + value));
                            break;
                        case 'subtract_time':
                            this.time = Math.max(0, this.time - value);
                            break;
                        case 'toggle_play_pause':
                            if (this.time > 0) {
                                this.isRunning = !this.isRunning;
                            }
                            break;
                        case 'stop':
                            this.isRunning = false;
                            break;
                    }
                    this.updateDisplay();
                }
                
                handleOfflineMode() {
                    this.isOnline = false;
                    this.stopPeriodicUpdate();
                    this.statusElement.textContent = "Modo offline - Funcionalidade limitada";
                    this.statusElement.style.color = '#fbbf24';
                }
                
                startPeriodicUpdate() {
                    this.stopPeriodicUpdate();
                    this.updateInterval = setInterval(() => {
                        if (this.isOnline) {
                            this.fetchTimerState();
                        }
                    }, 1000);
                }
                
                stopPeriodicUpdate() {
                    if (this.updateInterval) {
                        clearInterval(this.updateInterval);
                        this.updateInterval = null;
                    }
                }
                
                formatTime(timeInCentiseconds) {
                    const seconds = Math.floor(timeInCentiseconds / 100);
                    const centiseconds = timeInCentiseconds % 100;
                    return `${seconds.toString().padStart(2, '0')}.${centiseconds.toString().padStart(2, '0')}`;
                }
                
                getTimerColor() {
                    const timeInSeconds = this.time / 100;
                    if (timeInSeconds > 10) return 'timer-green';
                    if (timeInSeconds > 5) return 'timer-yellow';
                    return 'timer-red';
                }
                
                getBorderClass() {
                    const timeInSeconds = this.time / 100;
                    if (timeInSeconds > 10) return 'border-green';
                    if (timeInSeconds > 5) return 'border-yellow';
                    return 'border-red';
                }
                
                updateDisplay() {
                    // Atualizar texto do timer
                    this.timerElement.textContent = this.formatTime(this.time);
                    this.timerElement.className = `timer-text ${this.getTimerColor()}`;
                    
                    // Atualizar borda do display
                    this.timerDisplayElement.className = `timer-display ${this.getBorderClass()}`;
                    
                    // Atualizar botão play/pause
                    this.playPauseBtn.disabled = this.time === 0;
                    this.playPauseBtn.innerHTML = this.isRunning ? this.pauseIcon : this.playIcon;
                    
                    // Atualizar status
                    this.updateStatus();
                    
                    // Adicionar vibração em dispositivos móveis para feedback tátil
                    if (this.time <= 500 && this.time > 0 && this.isRunning && 'vibrate' in navigator) {
                        navigator.vibrate(100);
                    }
                }
                
                updateStatus() {
                    if (!this.isOnline) {
                        this.statusElement.textContent = "Modo offline - Funcionalidade limitada";
                        this.statusElement.style.color = '#fbbf24';
                        return;
                    }
                    
                    this.statusElement.style.color = '#9ca3af';
                    
                    if (this.time === 0) {
                        this.statusElement.textContent = "Pressione +24s ou +14s para começar";
                    } else if (!this.isRunning) {
                        this.statusElement.textContent = "Pressione play para iniciar";
                    } else {
                        this.statusElement.textContent = "Cronômetro ativo";
                    }
                }
                
                startLocalTimer() {
                    this.stopLocalTimer();
                    
                    this.intervalId = setInterval(() => {
                        if (this.time <= 0) {
                            this.stopLocalTimer();
                            this.isRunning = false;
                            this.updateDisplay();
                            return;
                        }
                        this.time--;
                        this.updateDisplay();
                    }, 10);
                }
                
                stopLocalTimer() {
                    if (this.intervalId) {
                        clearInterval(this.intervalId);
                        this.intervalId = null;
                    }
                }
                
                cleanup() {
                    this.stopLocalTimer();
                    this.stopPeriodicUpdate();
                }
                
                // Métodos públicos para os botões
                async setTime(seconds) {
                    const centiseconds = seconds * 100;
                    await this.updateTimerOnServer('set_time', centiseconds);
                    this.stopLocalTimer();
                }
                
                async addTime(seconds) {
                    const centiseconds = Math.round(seconds * 100);
                    await this.updateTimerOnServer('add_time', centiseconds);
                }
                
                async subtractTime(seconds) {
                    const centiseconds = Math.round(seconds * 100);
                    await this.updateTimerOnServer('subtract_time', centiseconds);
                }
                
                async togglePlayPause() {
                    if (this.time <= 0) return;
                    
                    await this.updateTimerOnServer('toggle_play_pause');
                    
                    // Controle local do timer para responsividade
                    if (this.isRunning) {
                        this.startLocalTimer();
                    } else {
                        this.stopLocalTimer();
                    }
                }
                
                async resetTimer() {
                    await this.updateTimerOnServer('set_time', 0);
                    this.stopLocalTimer();
                }
            }
            
            // Inicializar quando a página carregar
            let timer;
            document.addEventListener('DOMContentLoaded', () => {
                timer = new BasketballTimer();
            });
            
            // Funções globais para os botões (compatibilidade)
            function setTime(seconds) {
                if (timer) timer.setTime(seconds);
            }
            
            function addTime(seconds) {
                if (timer) timer.addTime(seconds);
            }
            
            function subtractTime(seconds) {
                if (timer) timer.subtractTime(seconds);
            }
            
            function togglePlayPause() {
                if (timer) timer.togglePlayPause();
            }
            
            // Service Worker para funcionalidade offline (opcional)
            if ('serviceWorker' in navigator) {
                window.addEventListener('load', () => {
                    navigator.serviceWorker.register('/static/sw.js').catch(err => {
                        console.log('Service Worker registration failed');
                    });
                });
            }
            
            // PWA - Add to Home Screen
            let deferredPrompt;
            window.addEventListener('beforeinstallprompt', (e) => {
                e.preventDefault();
                deferredPrompt = e;
                
                // Mostrar botão de instalação personalizado se desejar
                // showInstallButton();
            });
            
            // Performance - Preload critical resources
            const preloadLink = document.createElement('link');
            preloadLink.rel = 'preload';
            preloadLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css';
            preloadLink.as = 'style';
            document.head.appendChild(preloadLink);
        </script>
        
        <!-- Meta tags adicionais para PWA -->
        <meta name="theme-color" content="#0e1117">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="Cronômetro Basquete">
        
        <!-- Preconnect para melhor performance -->
        <link rel="preconnect" href="https://cdnjs.cloudflare.com">
        <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">
    </body>
    </html>
    """
    
    # Renderizar o componente HTML ocupando toda a tela
    components.html(html_code, height=1200, width=None, scrolling=False)


if __name__ == "__main__":
    main()