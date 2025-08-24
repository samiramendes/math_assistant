import chainlit as cl
from dotenv import load_dotenv
import os


load_dotenv()
llm_api_key = os.getenv("GROQ_API_KEY")

@cl.on_message
async def process_message(message: cl.Message):
    agent = cl.user_session.get("agent")

    response = await agent.ainvoke(message.content,
                                 callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(response["output"]).send()