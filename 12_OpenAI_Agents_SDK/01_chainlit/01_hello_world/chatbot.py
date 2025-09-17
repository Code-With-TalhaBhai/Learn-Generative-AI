import chainlit as cl


# command for chainlit through uv:
# 1. uv run chainlit run [filename](chatbot.py)
# 2. uv run chainlit run chatbot.py -w (for realtime changes)


@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Recieved: {message.content}").send()
