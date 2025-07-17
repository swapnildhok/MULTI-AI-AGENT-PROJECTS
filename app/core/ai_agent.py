from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings

def get_response_from_ai_agents(llm_id , query , allow_search ,system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    state = {
    "messages": [
        {"role": "system", "content": system_prompt},
        *[
            {"role": "user", "content": msg}
            for msg in query
        ]
    ]
}

    response = agent.invoke(state)

    messages = response.get("messages",[])

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1] if ai_messages else "No AI response generated."






