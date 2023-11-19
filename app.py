import gradio as gr
from image_analyser_gpt.ask_gpt import simple_prompt

MARKDOWN = """
# Art critique GPT

This is a demo of Art critique GPT, a tool that allows you to chat with a artwork using GPT-4. 
"""


def chat(image,API_KEY):
    """
    @brief Chat with the GPT-4 Vision model using the image and prompt provided.
    @param image The image to be used as the payload.
    @return The response from the GPT-4 Vision model.
    """
    with open("./prompt.txt", "r") as f:
        prompt = f.read()
    response = simple_prompt(image=image, prompt=prompt, api_key=API_KEY)
    return response

#gradio app build
with gr.Blocks() as demo:
    gr.Markdown(MARKDOWN)
    images = gr.Image(source="upload",streaming=False,type="pil")
    API_KEY = gr.Textbox(lines=1,label="Openai_API_KEY")
    gr.Interface(fn=chat,inputs=[images,API_KEY],outputs="text")

demo.launch()