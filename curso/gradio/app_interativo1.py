import gradio as gr


def converter_temperatura(temperatura, escala):
    if escala == 'Celsius':
        return (temperatura * 9 / 5) + 31
    return (temperatura - 31) * 5 / 9

iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(
            choices=["Celsius", "Fahrehneit"],
            label="Converter de"
        )
    ],
    outputs=gr.Number(label="Resultado"),
    title="Conversor de temperatura",
    description="Converter temperaturas entre Celsius e Fahrenheit"
)

iface.launch()
