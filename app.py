#imports
import gradio as gr
from backend import chat

#auth
import os
from dotenv import load_dotenv

load_dotenv()

auth = [
    (
        os.getenv("KIRAN_USERNAME"),
        os.getenv("KIRAN_PASSWORD")
    ),
    (
        os.getenv("CHINNU_USERNAME"),
        os.getenv("CHINNU_PASSWORD")
    )
]

#Css styling
css = """
body {
    margin: 0;
    background: #faf7f8;
}

.gradio-container {
    max-width: 100% !important;
    width: 100% !important;
    min-height: 100vh !important;
    padding: 0 !important;
}

#app-content {
    width: 100%;
    min-height: 100vh;
    padding: 30px 5%;
    box-sizing: border-box;
}

#title {
    text-align: center;
    margin-bottom: 8px;
}

#subtitle {
    text-align: center;
    color: #777;
    margin-bottom: 12px;
}

#privacy {
    text-align: center;
    font-size: 13px;
    color: #888;
    margin-bottom: 25px;
}


#mode-selector {
    max-width: 700px;
    margin: 0 auto 25px auto;
}

#mode-selector > label {
    text-align: center;
}

#mode-selector .wrap {
    justify-content: center;
    gap: 12px;
}

#mode-selector .wrap label {
    border-radius: 12px !important;
    padding: 10px 18px !important;
}

#chat-area {
    width: 100%;
    max-width: 1100px;
    margin: 0 auto;
}

#chat-area .bubble-wrap {
    border-radius: 18px !important;
}

#message-box {
    margin-top: 12px;
}

#message-box textarea {
    border-radius: 16px !important;
    padding: 14px 16px !important;
    font-size: 15px !important;
}

#message-box textarea:focus {
    box-shadow: none !important;
}

.section-label {
    font-weight: 600;
    margin-bottom: 8px;
}

/* Responsive spacing for smaller screens */
@media (max-width: 768px) {
    #app-content {
        padding: 20px 4%;
    }
}
"""
#API call
def chat_from_ui(message, history, partner, mode):

    history = history or []

    # Make sure history is in the format the backend expects
    clean_history = []

    for h in history:
        if isinstance(h, dict):
            clean_history.append({
                "role": h["role"],
                "content": h["content"]
            })
        else:
            clean_history.append({
                "role": h.role,
                "content": h.content
            })

    # Backend streams only the assistant text
    for response in chat(
        message,
        clean_history,
        partner,
        mode
    ):

        yield (
    clean_history + [
        {
            "role": "user",
            "content": message
        },
        {
            "role": "assistant",
            "content": response
        }
    ],
    ""
)

#Gradio ui
with gr.Blocks(
    title="Our Little Space",
) as demo:

    with gr.Column(elem_id="app-content"):

        gr.Markdown(
            """
            <div id="title">
                <h1>♡ Our Little Space</h1>
            </div>

            <div id="subtitle">
                A little place to understand each other.
            </div>

            <div id="privacy">
                🔒 Private • Just for the two of you
            </div>
            """
        )

        partner = gr.Dropdown(
            choices=["Kiran", "Chinnu"],
            value="Kiran",
            label="Who are you?"
        )

        mode = gr.Radio(
            choices=[
                "Understand",
                "Cheer me up",
                "Help me reply"
            ],
            value="Understand",
            label="What do you need?",
            elem_id="mode_selector"
        )

        chatbot = gr.Chatbot(
            height=500,
            placeholder="Your conversation will appear here...",
            elem_id="chat-area",
        )

        textbox = gr.Textbox(
            placeholder="Tell me what's happening...",
            show_label=False,
            elem_id="message-box",
            lines=1
        )

        textbox.submit(
            chat_from_ui,
            inputs=[textbox, chatbot, partner, mode],
            outputs=[chatbot,textbox]
        )

demo.launch(
    css=css,
    auth=auth
)
