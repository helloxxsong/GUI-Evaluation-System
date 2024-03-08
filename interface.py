import gradio as gr
import GLM4V_local


def upload_img(gr_img, chatbot):
    if gr_img is None:
        return None
    else:
        easy_prompt = "Play the role of a test user of a mobile phone GUI interface. Describe the GUI elements in the given interface and briefly evaluate usability."
        chatbot = chatbot + [[None, GLM4V_local.single_image(prompt=easy_prompt, image_path=gr_img)]]
        return chatbot, gr.update(interactive=False), gr.update(interactive=True, placeholder='按下回车发送'), gr.update(
            interactive=False)


def gradio_ask(user_message, chatbot):
    chatbot = chatbot + [[user_message, None]]
    return "", chatbot


def gradio_answer(chatbot):
    chatbot[-1][1] = ""
    return chatbot


def gradio_reset():
    return None, gr.update(value=None, interactive=True), gr.update(placeholder='请先上传图片',
                                                                    interactive=False), gr.update(
        interactive=True)


title = """<h1 align="center">智览分析系统 Demo</h1>"""
description = """<h3>请上传图片并开始对话！</h3>"""

with gr.Blocks() as demo:
    gr.Markdown(title)
    gr.Markdown(description)

    with gr.Row():
        with gr.Column(scale=1):
            image = gr.Image(type='filepath')
            upload_button = gr.Button(value="分析", variant="primary")
            save_button = gr.Button(value="导出", variant="secondary")
            clear = gr.Button("重启")

        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label='智览系统')
            text_input = gr.Textbox(label='用户', placeholder='请先上传图片', interactive=False)

    upload_button.click(fn=upload_img, inputs=[image, chatbot], outputs=[chatbot, image, text_input, upload_button])
    text_input.submit(fn=gradio_ask, inputs=[text_input, chatbot], outputs=[text_input, chatbot]).then(fn=gradio_answer,
                                                                                                       inputs=[chatbot],
                                                                                                       outputs=[
                                                                                                           chatbot])
    clear.click(fn=gradio_reset, inputs=[], outputs=[chatbot, image, text_input, upload_button])

if __name__ == "__main__":
    demo.launch()
