from app.analyst.agent import analyst_agent
from app.analyst.config import AnalystConfig
from app.analyst.tools import (
    get_user_memory, 
    save_user_memory,
    get_player_stats,
    generate_report,
    tavily_search_tool
)
from app.analyst.prompts import analyst_prompt
from app.football.models import PlayerStats, TeamStats, MatchAnalysis, TacticalInsights, HeadToHeadStats, OppositionAnalysis
from app.core.logging import logger

logger.info()



class AnalystService: 
    def __init__(self, agent=analyst_agent, config=AnalystConfig(), tools=[get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool]):
        self.agent = agent
        self.config = config
        self.tools = tools

    async def analyse_player(self, player_name: str, user_id: str) -> str:
        """ This method will be called to analyse an individual player
        based on the latest statistics and generate a report. It will also save the user's preferences and memory for future interactions.
        """
        player_stats = get_player_stats(player_name)
        if player_stats is None: 
            return f"No statistics found for player {player_name}."
        report = generate_report(player_name, player_stats)
        save_user_memory(user_id, {"last_analyzed_player": player_name, "report": report})
        return report
    
    
    
    async def analyse_team(self, team_name: str, user_id: str) -> str: 
        """ This method will be called to analyse a team based on their latest statistics and generate a report. It will also save the user's preferences and memory for future interactions.
        for simplicity, we will just return a placeholder report here.
        """
        team_stats = get_team_stats(team_name)
        if team_stats is None:
            return f"No statistics found for team {team_name}."
        report = generate_team_report(team_name, team_stats)
        save_user_memory(user_id, {"last_analyzed_team": team_name, "report": report})
        return report
    
    async def analyse_topic(self, topic: str, user_id: str) -> str:
        """ This method will be called to analyse a specific topic related to football, such as a recent match, a tactical analysis, or a player comparison. It will also save the user's preferences and memory for future interactions.
        for simplicity, we will just return a placeholder report here.
        """
        search_results = tavily_search_tool.run(topic)
        report = generate_topic_report(topic, search_results)
        save_user_memory(user_id, {"last_analyzed_topic": topic, "report": report})
        return report
    

    