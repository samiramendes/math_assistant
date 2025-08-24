import chainlit as cl
from langchain_groq import ChatGroq
from langchain.agents.agent_types import AgentType
from langchain.agents import initialize_agent
from dotenv import load_dotenv
import os
from tools.calculator import calculator
from tools.web_searcher import wikipedia_search

load_dotenv()
llm_api_key = os.getenv("GROQ_API_KEY")

custom_prefix = """
You are a smart assistant capable of answering user questions.
Your superpower is knowing when to use external tools to respond accurately.

You have access to the following tools:
- Calculator: use it for any math-related question, even if it seems simple (e.g., "What is 12 times 15?")
- Wikipedia Search: use it for questions about facts, people, places, or historical events (e.g., "Who was Albert Einstein?")

If it's not necessary to use a tool (for example, for general or opinion-based questions), answer using your own knowledge.

Important:
- Whenever a question involves numbers or calculations, use the Calculator tool.
- Do not try to do the math yourself. Use the appropriate tool.
- Be direct and concise in your answers.
""".strip()
    
@cl.on_chat_start
def math_assistent():
    # Create Groq LLM 
    llm = ChatGroq(model="moonshotai/kimi-k2-instruct", temperature=0.0)

    agent = initialize_agent(
        tools=[calculator, wikipedia_search],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        agent_kwargs={"prefix": custom_prefix},
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