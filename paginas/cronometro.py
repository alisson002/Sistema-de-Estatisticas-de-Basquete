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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cronômetro de Basquete</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html, body {
                height: 45vh;
                width: 100vw;
                background: linear-gradient(135deg, #0e1117, #0e1117);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Arial', sans-serif;
                overflow: hidden;
                margin-top: -35px; /* Reduzido de -100px para -35px (65% menor) */
            }

            .container {
                width: 31.5vw; /* Reduzido de 90vw para 31.5vw (65% menor) */
                max-width: 280px; /* Reduzido de 800px para 280px (65% menor) */
                min-width: 300px;
                height: 31.5vh; /* Reduzido de 90vh para 31.5vh (65% menor) */
                min-height: 400px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 1.4vh; /* Reduzido de 40px para 14px (65% menor) convertido para vh */
            }

            .timer-display {
                background: #030712;
                border-radius: 1.26vh; /* Reduzido de 36px para 12.6px (65% menor) convertido para vh */
                border: 0.315vh solid #4ade80; /* Verde por padrão */
                width: 100%;
                height: 13.125vh; /* Reduzido de 375px para 131.25px (65% menor) convertido para vh */
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6); /* Reduzido de 15px 40px para 5.25px 14px (65% menor) */
                margin-bottom: 0.7vh; /* Reduzido de 20px para 7px (65% menor) convertido para vh */
                transition: all 0.3s ease;
            }

            /* Classes para diferentes cores de borda e glow */
            .timer-display.border-green {
                border-color: #4ade80;
                box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6), 0 0 1vh rgba(74, 222, 128, 0.2);
            }

            .timer-display.border-yellow {
                border-color: #fbbf24;
                box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6), 0 0 1.5vh rgba(251, 191, 36, 0.4);
            }

            .timer-display.border-red {
                border-color: #ef4444;
                box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6), 0 0 2vh rgba(239, 68, 68, 0.6);
            }

            .timer-text {
                font-size: 6.3vh; /* Reduzido de 180px para 63px (65% menor) convertido para vh */
                font-weight: 900;
                font-family: 'Courier New', monospace;
                letter-spacing: 0.315vh; /* Reduzido de 9px para 3.15px (65% menor) convertido para vh */
                transition: color 0.3s ease;
            }

            .button-row {
                display: flex;
                gap: 1.4vh; /* Reduzido de 40px para 14px (65% menor) convertido para vh */
                margin-bottom: 0.7vh; /* Reduzido de 20px para 7px (65% menor) convertido para vh */
            }

            .button-row-small {
                display: flex;
                gap: 1.05vh; /* Reduzido de 30px para 10.5px (65% menor) convertido para vh */
                margin-bottom: 0.7vh; /* Reduzido de 20px para 7px (65% menor) convertido para vh */
            }

            .btn {
                border: none;
                border-radius: 50%;
                font-weight: bold;
                box-shadow: 0 0.21vh 0.7vh rgba(0, 0, 0, 0.4); /* Reduzido de 6px 20px para 2.1px 7px (65% menor) */
                transition: all 0.2s ease;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #FFFFFF;
                color: black;
                font-size: 0.63vh; /* Reduzido de 18px para 6.3px (65% menor) convertido para vh */
            }

            .btn:hover:not(:disabled) {
                transform: scale(1.05);
                background: #ea580c;
                box-shadow: 0 0.28vh 0.875vh rgba(0, 0, 0, 0.5); /* Reduzido de 8px 25px para 2.8px 8.75px (65% menor) */
            }

            .btn:active {
                transform: scale(0.95);
            }

            .btn:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }

            .btn-large {
                width: 4.2vh; /* Reduzido de 120px para 42px (65% menor) convertido para vh */
                height: 4.2vh; /* Reduzido de 120px para 42px (65% menor) convertido para vh */
                font-size: 0.84vh; /* Reduzido de 24px para 8.4px (65% menor) convertido para vh */
            }

            .btn-play {
                width: 4.9vh; /* Reduzido de 140px para 49px (65% menor) convertido para vh */
                height: 4.9vh; /* Reduzido de 140px para 49px (65% menor) convertido para vh */
                font-size: 0.98vh; /* Reduzido de 28px para 9.8px (65% menor) convertido para vh */
                margin: 0.7vh 0; /* Reduzido de 20px para 7px (65% menor) convertido para vh */
            }

            .btn-small {
                width: 3.5vh; /* Reduzido de 100px para 35px (65% menor) convertido para vh */
                height: 3.5vh; /* Reduzido de 100px para 35px (65% menor) convertido para vh */
                font-size: 0.63vh; /* Reduzido de 18px para 6.3px (65% menor) convertido para vh */
            }

            .status-text {
                text-align: center;
                color: #9ca3af;
                font-size: 0.63vh; /* Reduzido de 18px para 6.3px (65% menor) convertido para vh */
                margin-top: 0.7vh; /* Reduzido de 20px para 7px (65% menor) convertido para vh */
            }

            .play-icon, .pause-icon {
                width: 1.68vh; /* Reduzido de 48px para 16.8px (65% menor) convertido para vh */
                height: 1.68vh; /* Reduzido de 48px para 16.8px (65% menor) convertido para vh */
                pointer-events: none;
            }

            .play-icon {
                margin-left: 0.21vh; /* Reduzido de 6px para 2.1px (65% menor) convertido para vh */
            }

            /* Cores do timer baseadas no tempo */
            .timer-green { color: #4ade80; }
            .timer-yellow { color: #fbbf24; }
            .timer-red { color: #ef4444; }

            /* Responsividade para telas menores - 5% menor que as proporções originais */
            @media (max-width: 768px) {
                html, body {
                    margin-top: -130px; /* 5% menor que -100px original */
                    height: 100vh; /* Volta para 100vh no mobile */
                }

                .container {
                    width: 90.25vw; /* 5% menor que 95vw original */
                    height: auto;
                    min-height: auto;
                    gap: 28.5px; /* 5% menor que 30px original - valores fixos para mobile */
                }
                
                .timer-display {
                    height: 285px; /* 5% menor que 300px original */
                    border-radius: 28.5px; /* 5% menor que 30px original */
                    border: 6.65px solid #4ade80; /* Verde por padrão - 5% menor que 7px original */
                    margin-bottom: 19px;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6); /* Sombra fixa para mobile */
                }

                .timer-display.border-green {
                    border-color: #4ade80;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(74, 222, 128, 0.2);
                }

                .timer-display.border-yellow {
                    border-color: #fbbf24;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 30px rgba(251, 191, 36, 0.4);
                }

                .timer-display.border-red {
                    border-color: #ef4444;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 40px rgba(239, 68, 68, 0.6);
                }
                
                .timer-text {
                    font-size: 128.25px; /* 5% menor que 135px original */
                    letter-spacing: 5.7px; /* 5% menor que 6px original */
                }
                
                .btn-large {
                    width: 95px; /* 5% menor que 100px original */
                    height: 95px; /* 5% menor que 100px original */
                    font-size: 19px; /* 5% menor que 20px original */
                }
                
                .btn-play {
                    width: 114px; /* 5% menor que 120px original */
                    height: 114px; /* 5% menor que 120px original */
                    font-size: 22.8px; /* 5% menor que 24px original */
                    margin: 19px 0;
                }
                
                .btn-small {
                    width: 76px; /* 5% menor que 80px original */
                    height: 76px; /* 5% menor que 80px original */
                    font-size: 15.2px; /* 5% menor que 16px original */
                }
                
                .button-row {
                    gap: 28.5px; /* 5% menor que 30px original */
                    margin-bottom: 19px;
                }
                
                .button-row-small {
                    gap: 19px; /* 5% menor que 20px original */
                    margin-bottom: 19px;
                }

                .btn {
                    font-size: 17.1px; /* 5% menor que 18px original */
                    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
                }

                .btn:hover:not(:disabled) {
                    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
                }

                .status-text {
                    font-size: 17.1px; /* 5% menor que 18px original */
                    margin-top: 19px;
                }

                .play-icon, .pause-icon {
                    width: 45.6px; /* 5% menor que 48px original */
                    height: 45.6px; /* 5% menor que 48px original */
                }

                .play-icon {
                    margin-left: 5.7px; /* 5% menor que 6px original */
                }
            }

            @media (max-width: 480px) {
                .container {
                    gap: 22px;
                }

                .timer-text {
                    font-size: 75px; /* 5% menor que 105px original */
                    letter-spacing: 2.85px; /* 5% menor que 3px original */
                }
                
                .timer-display {
                    height: 228px; /* 5% menor que 240px original */
                    border-radius: 22.8px; /* 5% menor que 24px original */
                    border: 4.75px solid #4ade80; /* Verde por padrão - 5% menor que 5px original */
                    margin-bottom: 15px;
                }

                .timer-display.border-green {
                    border-color: #4ade80;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 15px rgba(74, 222, 128, 0.2);
                }

                .timer-display.border-yellow {
                    border-color: #fbbf24;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(251, 191, 36, 0.4);
                }

                .timer-display.border-red {
                    border-color: #ef4444;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 35px rgba(239, 68, 68, 0.6);
                }
                
                .btn-large {
                    width: 76px; /* 5% menor que 80px original */
                    height: 76px; /* 5% menor que 80px original */
                    font-size: 17.1px; /* 5% menor que 18px original */
                }
                
                .btn-play {
                    width: 95px; /* 5% menor que 100px original */
                    height: 95px; /* 5% menor que 100px original */
                    font-size: 19px; /* 5% menor que 20px original */
                    margin: 15px 0;
                }
                
                .btn-small {
                    width: 66.5px; /* 5% menor que 70px original */
                    height: 66.5px; /* 5% menor que 70px original */
                    font-size: 13.3px; /* 5% menor que 14px original */
                }
                
                .button-row {
                    gap: 19px; /* 5% menor que 20px original */
                    margin-bottom: 15px;
                }
                
                .button-row-small {
                    gap: 14.25px; /* 5% menor que 15px original */
                    margin-bottom: 15px;
                }
                
                .status-text {
                    font-size: 15.2px; /* 5% menor que 16px original */
                    margin-top: 15px;
                }
            }

            /* Ajustes para telas muito grandes */
            @media (min-width: 1200px) {
                .container {
                    max-width: 320px; /* Proporcionalmente maior que 280px */
                }
            }

            @media (min-width: 1600px) {
                .container {
                    max-width: 360px; /* Proporcionalmente maior que 280px */
                }
            }

            @media (min-width: 2000px) {
                .container {
                    max-width: 420px; /* Proporcionalmente maior que 280px */
                }
            }

            /* Ajustes para telas muito pequenas em altura no desktop */
            @media (max-height: 600px) and (min-width: 769px) {
                html, body {
                    height: 90vh; /* Aumenta um pouco para telas baixas */
                    margin-top: -40px; /* Reduz margin para aproveitar espaço */
                }

                .container {
                    height: 80vh;
                    gap: 1.5vh;
                }
                
                .timer-display {
                    height: 18vh;
                    border-radius: 1.5vh;
                    border: 0.4vh solid #4ade80; /* Verde por padrão */
                    margin-bottom: 0.8vh;
                }

                .timer-display.border-green {
                    border-color: #4ade80;
                    box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6), 0 0 1vh rgba(74, 222, 128, 0.2);
                }

                .timer-display.border-yellow {
                    border-color: #fbbf24;
                    box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6), 0 0 1.5vh rgba(251, 191, 36, 0.4);
                }

                .timer-display.border-red {
                    border-color: #ef4444;
                    box-shadow: 0 0.525vh 1.4vh rgba(0, 0, 0, 0.6), 0 0 2vh rgba(239, 68, 68, 0.6);
                }
                
                .timer-text {
                    font-size: 8vh;
                    letter-spacing: 0.4vh;
                }
                
                .btn-large {
                    width: 5vh;
                    height: 5vh;
                    font-size: 1vh;
                }
                
                .btn-play {
                    width: 6vh;
                    height: 6vh;
                    font-size: 1.2vh;
                    margin: 0.8vh 0;
                }
                
                .btn-small {
                    width: 4vh;
                    height: 4vh;
                    font-size: 0.8vh;
                }
                
                .status-text {
                    font-size: 0.8vh;
                    margin-top: 0.8vh;
                }
                
                .play-icon, .pause-icon {
                    width: 2vh;
                    height: 2vh;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Display do cronômetro -->
            <div id="timerDisplay" class="timer-display border-green">
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
            const timerDisplayElement = document.getElementById('timerDisplay');
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

            // Determinar classe de borda baseada no tempo
            function getBorderClass() {
                const timeInSeconds = time / 100;
                if (timeInSeconds > 10) return 'border-green';
                if (timeInSeconds > 5) return 'border-yellow';
                return 'border-red';
            }

            // Atualizar display
            function updateDisplay() {
                timerElement.textContent = formatTime(time);
                timerElement.className = `timer-text ${getTimerColor()}`;
                
                // Atualizar borda do display
                timerDisplayElement.className = `timer-display ${getBorderClass()}`;
                
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