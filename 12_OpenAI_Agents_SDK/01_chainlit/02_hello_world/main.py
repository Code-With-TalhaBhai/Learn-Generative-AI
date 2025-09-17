import chainlit as cl



@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="New chat has started").send()


@cl.on_message
async def on_message(msg: cl.Message):
    await cl.Message(content=f'The user is: {msg.content}').send()



@cl.on_chat_end
async def on_chat_end():
    await cl.Message(content="Hope! You enjoyed it, if there is any other query I can resolve")



