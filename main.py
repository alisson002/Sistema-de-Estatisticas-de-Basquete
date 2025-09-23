import streamlit as st
from st_pages import add_page_title

# Estrutura de navegação do sistema
# O dicionário "pages" organiza as categorias e páginas do sistema
pages = {
    
    "": 
    [st.Page("paginas/inicio.py", title="Início", icon="🏀", default=True)],
    
    "🏆 Campeonatos": [
        
        st.Page("paginas/competicoes.py", title="Competição",icon="🥇"),
        st.Page("paginas/equipes.py", title="Equipes",icon="💪"),
    ],
    
    "🏅 Ranking Geral": [
        
        st.Page("paginas/atletas.py", title="Atletas", icon="⛹🏿‍♂️"),
        st.Page("paginas/times.py", title="Times", icon="👊"),
        
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


# # LOGIN
# import streamlit as st

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     if st.button("Log in"):
#         st.session_state.logged_in = True
#         st.rerun()

# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()

# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# #LOGIN

# inicio = st.Page("paginas/inicio.py", title="Início", icon="🏀", default=True)
# competicao = st.Page("paginas/competicoes.py", title="Competição",icon="🥇")
# equipes = st.Page("paginas/equipes.py", title="Equipes",icon="💪")
# atletas = st.Page("paginas/atletas.py", title="Atletas", icon="⛹🏿‍♂️")
# times = st.Page("paginas/times.py", title="Times", icon="👊")

# if st.session_state.logged_in:
#     pg = st.navigation(
#         {
            
#             "": [inicio],
#             "🏆 Campeonatos": [competicao, equipes],
#             "🏅 Ranking Geral": [atletas, times],
#             "Conta": [logout_page],
#         }
#     )
# else:
#     pg = st.navigation([login_page])

# pg.run()