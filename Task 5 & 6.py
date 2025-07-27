
def squarecalculatinfunction(number):
    return number * number

print(squarecalculatinfunction(34))
import gradio as gr

def squarecalculatinfunction(number):
    return number * number

iface = gr.Interface(
    fn=squarecalculatinfunction,
    inputs=gr.Number(label="Enter a number"),
    outputs=gr.Number(label="Square")
)

iface.launch()