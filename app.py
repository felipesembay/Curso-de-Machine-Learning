import streamlit as st
from pages import pagina1, pagina2

# Definir as páginas
paginas = {
    "Página 1": pagina1,
    "Página 2": pagina2
}

# Criar um seletor de páginas
pagina_selecionada = st.sidebar.selectbox("Escolha uma página", paginas.keys())

# Mostrar a página selecionada
paginas[pagina_selecionada].show()
