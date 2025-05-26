import requests
import streamlit as st


def pesquisar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    return response.json()['lyrics'] if response.status_code == 200 else ''


st.image(
    "https://img.freepik.com/fotos-premium/uma-colecao-de-musica-e-musica-incluindo-uma-foto-de-um-tocador-de-musica_1109006-146675.jpg")
st.title('Letras de músicas')

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = pesquisar_letra(banda, musica)

    if letra:
        st.success("Letra encontrada!")
        st.text(letra)
    else:
        st.error("Letra não encontrada.")
