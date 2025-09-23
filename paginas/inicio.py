import streamlit as st
from PIL import Image

image_placeholder = st.empty()

SEB_image_path = Image.open("imagens/fnblogo.png")
# image_placeholder.image(TN_image_path, use_column_width=True)

image_placeholder2 = st.empty()
SEB_image_path2 = Image.open("imagens/natalescudo.png")
# image_placeholder2.image(TN_image_path2, use_column_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image(SEB_image_path)
with col2:
    st.image(SEB_image_path2)

st.markdown(
    """
    <style>
    .nav-bar {
        font-size: 12px;
        text-align: justify;
    }
    .nav-item {
        text-align: Right;
    }
    </style>
    """,
    unsafe_allow_html=True,
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