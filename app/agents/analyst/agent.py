
from langchain.agents import create_agent, AgentSate
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import (
    SummarizationMiddleware, 
    ModelCallLimitMiddlware, 
    ToolRetryMiddleware, 
    ModelFallbackMiddleware
)
from app.agents.analyst.tools import 
from app.core.settings import settings
from app.agents.analyst.config import AnalystConfig
from app.agents.analyst.prompts import analyst_prompt
from app.agents.analyst.tools import get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool



class CustomAgentState(AgentState):
    user_id = int
    preferences: dict


model = ChatOpenAI(
    model= "openai:gpt-5.4",
    temperature=AnalystConfig.temprature,
    max_tokens=AnalystConfig.max_tokens,

)

sub_agent = create_agent(
    model=model,
    tools = [tool]
)

@tool

analyst_agent = create_agent(
    model= model.model,
    system_prompt=analyst_prompt,
    tools=[get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool],
    middleware=[
        SummarizationMiddleware(
            model="gpt-5.4-mini",
            trigger=("tokens", 4000),
            keep=("messages", 20)
        ),
        ModelCallLimitMiddlware(
            thread_limit=10,
            run_limit=5,
            exit_behavior="end"
        ),
        ModelFallbackMiddleware(
            "gpt-5.4-mini",
        ),

    ]

)



