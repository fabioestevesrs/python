import gradio as gr
import string
from collections import Counter

def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans("", "", string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)

    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])

    return num_palavras, num_caracteres, frequencia_html

iface = gr.Interface(
    fn=analisar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite o texto aqui", lines=6)
    ],
    outputs=[
        gr.Number(label="Número de palavras"),
        gr.Number(label="Número de caracteres"),
        gr.HTML(label="Frequência de palavras")
    ],
    title="Analisador de texto",
    description="Insira um texto e obtenha análises sobre ele"
)

iface.launch()