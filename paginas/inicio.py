import streamlit as st
from PIL import Image
from functions.manipulacao_de_imagem import img_to_base64 # Importa a função para manipulação de imagens, que será usada para centralizar.

# Faz com que a opção "[] Wide Mode" fique sempre selecionada, ou seja, a página sempre abrirá em modo wide. Sendo assim, as informações ficarão mais distribuídas na tela.
st.set_page_config(
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
        'Get Help': 'mailto:am.analistadedados@gmail.com',
        'Report a bug': 'mailto:am.analistadedados@gmail.com',
        'About': "Aplicação feita com Streamlit para visualização de dados financeiros do Grupo Allure. \n\n Entre em contato: am.analistadedados@gmail.com"
        }
)

image_placeholder = st.empty()

SEB_image_path = Image.open("imagens/fnblogo.png")
# image_placeholder.image(TN_image_path, use_column_width=True)

# Converter a imagem
# A função img_to_base64 converte a imagem para base64, que é um formato que pode ser embutido diretamente no HTML, permitindo a centralização da imagem.
# Recebe a imagem e retorna a string em base64.
img_base64 = img_to_base64(SEB_image_path)

image_placeholder2 = st.empty()
SEB_image_path2 = Image.open("imagens/natalescudo.png")

img_base64_2 = img_to_base64(SEB_image_path2)

st.markdown(
    """
    <style>
    .nav-bar {
        font-size: 24px;
        text-align: center;
    }
    .nav-item {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibir com HTML as imagens
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_base64}" width="600" />
        <img src="data:image/png;base64,{img_base64_2}" width="600" />
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="nav-bar">
        <p>
        Este sistema foi desenvolvido com o objetivo de centralizar, organizar e exibir dados estatísticos de atletas, equipes e campeonatos locais de basquete em Natal-RN e região. Através da coleta e visualização de dados de desempenho individual e coletivo, a plataforma busca facilitar o acompanhamento da evolução dos jogadores e oferecer uma visão mais completa sobre o cenário do basquete local.
        </p>
        <p>
        A proposta é que atletas, técnicos e entusiastas do esporte possam utilizar o sistema como uma ferramenta de consulta, análise e valorização do basquete regional. Ao consolidar informações em um só lugar, o sistema contribui para dar visibilidade aos talentos locais, fomentar a competitividade saudável entre equipes e apoiar iniciativas voltadas ao desenvolvimento esportivo.
        </p>
        <p class="nav-item"><b>Criado por:</b> Alisson Moreira.</p>
    </div>
    """,
    unsafe_allow_html=True
)