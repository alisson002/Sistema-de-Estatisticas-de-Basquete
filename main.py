import streamlit as st
from st_pages import add_page_title

import streamlit as st
from st_pages import add_page_title

# CSS para aumentar a fonte da barra lateral
st.markdown(
    """
    <style>
    /* Aumentar fonte dos títulos das seções (🏆 Campeonatos, 🏅 Ranking Geral, etc.) */
    .st-emotion-cache-1bgz58e {
        font-size: 24px !important;
        font-weight: bold !important;
    }
    
    /* Aumentar fonte do "Início" e deixar em negrito */
    .st-emotion-cache-b4a1cq {
        font-size: 24px !important;
        font-weight: bold !important;
    }
    
    /* Forçar negrito especificamente na barra lateral */
    [data-testid="stSidebarNav"] .st-emotion-cache-b4a1cq {
        font-weight: bold !important;
    }
    
    /* Alternativa mais específica para links na sidebar */
    [data-testid="stSidebarNavLink"][aria-current="page"] span[label="Início"] {
        font-weight: bold !important;
    }
    
    /* Aumentar fonte dos outros nomes das páginas individuais */
    .st-emotion-cache-kbwqmw,
    .st-emotion-cache-1lhpvq6,
    .st-emotion-cache-19q0fwg,
    .st-emotion-cache-wcsic8,
    .st-emotion-cache-1ne06is,
    .st-emotion-cache-fxurbn {
        font-size: 24px !important;
        font-weight: 500 !important;
    }
    
    /* Aumentar fonte dos emojis/ícones */
    .st-emotion-cache-1u1i2v4 {
        font-size: 26px !important;
    }
    
    /* Alternativa mais segura - usar seletores de atributos */
    [data-testid="stNavSectionHeader"] span {
        font-size: 26px !important;
        font-weight: bold !important;
    }
    
    /* Aumentar fonte de todos os links de navegação */
    [data-testid="stSidebarNavLink"] span[label] {
        font-size: 24px !important;
        font-weight: 500 !important;
    }
    
    /* Aumentar fonte de toda a área de navegação como fallback */
    [data-testid="stSidebarNav"] {
        font-size: 24px !important;
    }
    
    /* Ajustar espaçamento para acomodar fonte maior */
    [data-testid="stSidebarNavLink"] {
        padding: 8px 12px !important;
        line-height: 1.4 !important;
    }
    
    /* Forçar negrito com máxima especificidade */
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] .st-emotion-cache-1o8ztgu {
        font-weight: bold !important;
    }
    
    @media (max-width: 768px) {
        section[data-testid="stSidebar"] {
            width: 500px !important;
            min-width: 500px !important;
            max-width: 500px !important;
        }
    }
    
    section[data-testid="stSidebar"] {
        width: 380px !important;        /* Sua largura desejada */
        min-width: 380px !important;    /* Mesma largura mínima */
        max-width: 380px !important;    /* Mesma largura máxima */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Estrutura de navegação do sistema
# O dicionário "pages" organiza as categorias e páginas do sistema
pages = {
    
    "": 
    [st.Page("paginas/inicio.py", title="🏀 Início", default=True)],
    
    "🏆 Campeonatos": [
        
        st.Page("paginas/competicoes.py", title="🥇 Competição"),
        st.Page("paginas/equipes.py", title="💪 Equipes"),
    ],
    
    "🏅 Ranking Geral": [
        
        st.Page("paginas/atletas.py", title="⛹🏿‍♂️ Atletas"),
        st.Page("paginas/times.py", title="👊 Times"),
        
    ],
    
    "👨🏾‍💻 Outros Projetos": [
        
        st.Page("paginas/detector_sinalizacao.py", title="🕵🏾 Detector de Sinalização"),
        st.Page("paginas/cronometro.py", title="⏱️ Cronômetro 24/14"),
        
    ],
    
}

# Criação do menu de navegação
# O método st.navigation utiliza a estrutura definida no dicionário "pages" para criar um menu interativo
pg = st.navigation(pages)

# Adiciona o título personalizado para a página ativa
# Utiliza o título definido em cada página do dicionário "pages"
add_page_title(pg)

# Executa a página selecionada pelo usuário
# O método run() carrega e exibe a lógica da página correspondente no menu
pg.run()