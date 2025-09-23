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
    header {visibility: visible;}
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
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # HTML com React compilado (usando CDN)
    html_code = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cronômetro de Basquete</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html, body {
                height: 100vh;
                width: 100vw;
                background: linear-gradient(135deg, #0e1117, #0e1117);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Arial', sans-serif;
                overflow: hidden;
                margin-top: -100px;
            }

            .container {
                width: 45vw; /* 50% menor que 90vw para desktop */
                max-width: 400px; /* 50% menor que 800px para desktop */
                height: 45vh; /* 50% menor que 90vh para desktop */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 20px; /* 50% menor que 40px para desktop */
            }

            .timer-display {
                background: #030712;
                border-radius: 18px; /* 50% menor que 36px */
                border: 5px solid #FFFFFF; /* Aproximadamente 50% menor que 9px */
                width: 100%;
                height: 187px; /* 50% menor que 375px */
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6); /* Ajustado proporcionalmente */
                margin-bottom: 10px; /* 50% menor que 20px */
            }

            .timer-text {
                font-size: 90px; /* 50% menor que 180px */
                font-weight: 900;
                font-family: 'Courier New', monospace;
                letter-spacing: 4px; /* Aproximadamente 50% menor que 9px */
                transition: color 0.3s ease;
            }

            .button-row {
                display: flex;
                gap: 20px; /* 50% menor que 40px */
                margin-bottom: 10px; /* 50% menor que 20px */
            }

            .button-row-small {
                display: flex;
                gap: 15px; /* 50% menor que 30px */
                margin-bottom: 10px; /* 50% menor que 20px */
            }

            .btn {
                border: none;
                border-radius: 50%;
                font-weight: bold;
                box-shadow: 0 3px 10px rgba(0, 0, 0, 0.4); /* Ajustado proporcionalmente */
                transition: all 0.2s ease;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #FFFFFF;
                color: black;
                font-size: 9px; /* 50% menor que 18px */
            }

            .btn:hover:not(:disabled) {
                transform: scale(1.05);
                background: #ea580c;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5); /* Ajustado */
            }

            .btn:active {
                transform: scale(0.95);
            }

            .btn:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }

            .btn-large {
                width: 60px; /* 50% menor que 120px */
                height: 60px; /* 50% menor que 120px */
                font-size: 12px; /* 50% menor que 24px */
            }

            .btn-play {
                width: 70px; /* 50% menor que 140px */
                height: 70px; /* 50% menor que 140px */
                font-size: 14px; /* 50% menor que 28px */
                margin: 10px 0; /* 50% menor que 20px 0 */
            }

            .btn-small {
                width: 50px; /* 50% menor que 100px */
                height: 50px; /* 50% menor que 100px */
                font-size: 9px; /* 50% menor que 18px */
            }

            .status-text {
                text-align: center;
                color: #9ca3af;
                font-size: 9px; /* 50% menor que 18px */
                margin-top: 10px; /* 50% menor que 20px */
            }

            .play-icon, .pause-icon {
                width: 24px; /* 50% menor que 48px */
                height: 24px; /* 50% menor que 48px */
                pointer-events: none;
            }

            .play-icon {
                margin-left: 3px; /* Ajustado proporcionalmente */
            }

            /* Cores do timer baseadas no tempo */
            .timer-green { color: #4ade80; }
            .timer-yellow { color: #fbbf24; }
            .timer-red { color: #ef4444; }

            /* Responsividade para tablets */
            @media (max-width: 1024px) {
                .container {
                    width: 60vw;
                    max-width: 500px;
                    height: 60vh;
                    gap: 25px;
                }
                
                .timer-display {
                    height: 230px;
                    border-radius: 22px;
                    border: 6px solid #FFFFFF;
                }
                
                .timer-text {
                    font-size: 110px;
                    letter-spacing: 5px;
                }
                
                .btn-large {
                    width: 75px;
                    height: 75px;
                    font-size: 15px;
                }
                
                .btn-play {
                    width: 85px;
                    height: 85px;
                    font-size: 17px;
                }
                
                .btn-small {
                    width: 65px;
                    height: 65px;
                    font-size: 12px;
                }
                
                .status-text {
                    font-size: 12px;
                }
                
                .play-icon, .pause-icon {
                    width: 30px;
                    height: 30px;
                }
            }

            /* Responsividade para celular - 15% menor que o original */
            @media (max-width: 768px) {
                .container {
                    width: 80vw; /* 15% menor que 95vw */
                    gap: 25px; /* 15% menor que 30px */
                }
                
                .timer-display {
                    height: 255px; /* 15% menor que 300px */
                    border-radius: 25px; /* 15% menor que 30px */
                    border: 6px solid #f97316; /* 15% menor que 7px */
                }
                
                .timer-text {
                    font-size: 115px; /* 15% menor que 135px */
                    letter-spacing: 5px; /* 15% menor que 6px */
                }
                
                .btn-large {
                    width: 85px; /* 15% menor que 100px */
                    height: 85px; /* 15% menor que 100px */
                    font-size: 17px; /* 15% menor que 20px */
                }
                
                .btn-play {
                    width: 102px; /* 15% menor que 120px */
                    height: 102px; /* 15% menor que 120px */
                    font-size: 20px; /* 15% menor que 24px */
                }
                
                .btn-small {
                    width: 68px; /* 15% menor que 80px */
                    height: 68px; /* 15% menor que 80px */
                    font-size: 14px; /* 15% menor que 16px */
                }
                
                .button-row {
                    gap: 25px; /* 15% menor que 30px */
                }
                
                .button-row-small {
                    gap: 17px; /* 15% menor que 20px */
                }
                
                .play-icon, .pause-icon {
                    width: 36px; /* Ajustado proporcionalmente */
                    height: 36px;
                }
                
                .status-text {
                    font-size: 15px; /* 15% menor que 18px */
                }
            }

            @media (max-width: 480px) {
                .timer-text {
                    font-size: 89px; /* 15% menor que 105px */
                    letter-spacing: 2px; /* 15% menor que 3px */
                }
                
                .timer-display {
                    height: 204px; /* 15% menor que 240px */
                    border-radius: 20px; /* 15% menor que 24px */
                    border: 4px solid #f97316; /* 15% menor que 5px */
                }
                
                .btn-large {
                    width: 68px; /* 15% menor que 80px */
                    height: 68px; /* 15% menor que 80px */
                    font-size: 15px; /* 15% menor que 18px */
                }
                
                .btn-play {
                    width: 85px; /* 15% menor que 100px */
                    height: 85px; /* 15% menor que 100px */
                    font-size: 17px; /* 15% menor que 20px */
                }
                
                .btn-small {
                    width: 59px; /* 15% menor que 70px */
                    height: 59px; /* 15% menor que 70px */
                    font-size: 12px; /* 15% menor que 14px */
                }
                
                .button-row {
                    gap: 17px; /* 15% menor que 20px */
                }
                
                .button-row-small {
                    gap: 13px; /* 15% menor que 15px */
                }
                
                .status-text {
                    font-size: 14px; /* 15% menor que 16px */
                }
                
                .play-icon, .pause-icon {
                    width: 30px;
                    height: 30px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Display do cronômetro -->
            <div class="timer-display">
                <div id="timer" class="timer-text timer-green">00.00</div>
            </div>

            <!-- Botões superiores: +24s e +14s -->
            <div class="button-row">
                <button class="btn btn-large" onclick="start24()">+24s</button>
                <button class="btn btn-large" onclick="start14()">+14s</button>
            </div>

            <!-- Botão central: Play/Pause -->
            <div>
                <button id="playPauseBtn" class="btn btn-play" onclick="togglePlayPause()" disabled>
                    <svg class="play-icon" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M8 5v14l11-7z"/>
                    </svg>
                </button>
            </div>

            <!-- Botões inferiores: +1s, +0.1s, +0.01s -->
            <div class="button-row-small">
                <button class="btn btn-small" onclick="add1s()">+1s</button>
                <button class="btn btn-small" onclick="add01s()">+0.1s</button>
                <button class="btn btn-small" onclick="add001s()">+0.01s</button>
            </div>

            <!-- Botões inferiores: -1s, -0.1s, -0.01s -->
            <div class="button-row-small">
                <button class="btn btn-small" onclick="sub1s()">-1s</button>
                <button class="btn btn-small" onclick="sub01s()">-0.1s</button>
                <button class="btn btn-small" onclick="sub001s()">-0.01s</button>
            </div>

            <!-- Indicador de status -->
            <div id="status" class="status-text">
                Pressione +24s ou +14s para começar
            </div>
        </div>

        <script>
            let time = 0; // em centésimos de segundo
            let isRunning = false;
            let intervalId = null;

            // Elementos DOM
            const timerElement = document.getElementById('timer');
            const playPauseBtn = document.getElementById('playPauseBtn');
            const statusElement = document.getElementById('status');

            // Ícones SVG
            const playIcon = `
                <svg class="play-icon" viewBox="0 0 24 24" fill="currentColor" style="pointer-events: none;">
                    <path d="M8 5v14l11-7z"/>
                </svg>
            `;
            
            const pauseIcon = `
                <svg class="pause-icon" viewBox="0 0 24 24" fill="currentColor" style="pointer-events: none;">
                    <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
                </svg>
            `;

            // Formatar tempo para 00.00
            function formatTime(timeInCentiseconds) {
                const seconds = Math.floor(timeInCentiseconds / 100);
                const centiseconds = timeInCentiseconds % 100;
                return `${seconds.toString().padStart(2, '0')}.${centiseconds.toString().padStart(2, '0')}`;
            }

            // Determinar cor baseada no tempo
            function getTimerColor() {
                const timeInSeconds = time / 100;
                if (timeInSeconds > 10) return 'timer-green';
                if (timeInSeconds > 5) return 'timer-yellow';
                return 'timer-red';
            }

            // Atualizar display
            function updateDisplay() {
                timerElement.textContent = formatTime(time);
                timerElement.className = `timer-text ${getTimerColor()}`;
                
                // Atualizar botão play/pause
                playPauseBtn.disabled = time === 0;
                playPauseBtn.innerHTML = isRunning ? pauseIcon : playIcon;
                
                // Atualizar status
                if (time === 0) {
                    statusElement.textContent = "Pressione +24s ou +14s para começar";
                } else if (!isRunning) {
                    statusElement.textContent = "Pressione play para iniciar";
                } else {
                    statusElement.textContent = "Cronômetro ativo";
                }
            }

            // Iniciar/parar o cronômetro
            function startTimer() {
                if (intervalId) clearInterval(intervalId);
                
                intervalId = setInterval(() => {
                    if (time <= 0) {
                        stopTimer();
                        return;
                    }
                    time--;
                    updateDisplay();
                }, 10); // atualiza a cada centésimo de segundo
            }

            function stopTimer() {
                isRunning = false;
                if (intervalId) {
                    clearInterval(intervalId);
                    intervalId = null;
                }
                updateDisplay();
            }

            // Funções dos botões
            function start24() {
                time = 2400; // 24 segundos
                isRunning = false;
                stopTimer();
                updateDisplay();
            }

            function start14() {
                time = 1400; // 14 segundos
                isRunning = false;
                stopTimer();
                updateDisplay();
            }

            function add1s() {
                time = Math.min(time + 100, 2400); // máximo 24s
                updateDisplay();
            }

            function add01s() {
                time = Math.min(time + 10, 2400); // máximo 24s
                updateDisplay();
            }

            function add001s() {
                time = Math.min(time + 1, 2400); // máximo 24s
                updateDisplay();
            }

            function sub1s() {
                time = Math.max(time - 100, 0); // mínimo 0s
                updateDisplay();
            }

            function sub01s() {
                time = Math.max(time - 10, 0); // mínimo 0s
                updateDisplay();
            }

            function sub001s() {
                time = Math.max(time - 1, 0); // mínimo 0s
                updateDisplay();
            }

            function togglePlayPause() {
                if (time <= 0) return;
                
                isRunning = !isRunning;
                
                if (isRunning) {
                    startTimer();
                } else {
                    stopTimer();
                }
            }

            // Inicializar display
            updateDisplay();

            // Cleanup ao fechar a página
            window.addEventListener('beforeunload', () => {
                if (intervalId) clearInterval(intervalId);
            });
        </script>
    </body>
    </html>
    """
    
    # Renderizar o componente HTML ocupando toda a tela
    components.html(html_code, height=1200, width=None, scrolling=False)


if __name__ == "__main__":
    main()