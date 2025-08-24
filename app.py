import chainlit as cl
from langchain_groq import ChatGroq
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from dotenv import load_dotenv
import os
from tools.calculator import calculator
from tools.web_searcher import wikipedia_search

load_dotenv()
llm_api_key = os.getenv("GROQ_API_KEY")

    
@cl.on_chat_start
def math_assistent():
    # Create Groq LLM 
    llm = ChatGroq(model="moonshotai/kimi-k2-instruct", temperature=0.0)

    agent = initialize_agent(
        tools=[calculator, wikipedia_search],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )
    cl.user_session.set("agent", agent)

@cl.on_message
async def process_message(message: cl.Message):
    agent = cl.user_session.get("agent")

    response = await agent.ainvoke(message.content,
                                 callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(response["output"]).send()