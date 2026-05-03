from typing import List, Any

from app.agents.analyst.agent import analyst_agent
from app.agents.analyst.config import AnalystConfig
from app.agents.analyst.repository import AnalystRepository
from app.agents.analyst.models import AnalysisType, AnalysisStatus


class AnalystService: 
    def __init__(self, analyst_agent):
        self.agent = agent
        self.config = config
        self.tools = tools
        self.analysis_status = analysis_status
        self.repository = repository
    
    async def run_analysis(self, team_name: str, user_id: str) -> Analysis: 
        """ This method will be called to analyse a team based on their latest statistics and generate a report. It will also save the user's preferences and memory for future interactions.
        for simplicity, we will just return a placeholder report here.
        """
        if not team_name: 
            raise InvalidInputExecption(f"team is required to run an analysis.")
        
        analysis = Analysis(
            topic=["team_analysis", team_name],
            input=f"Analyse {team_name}"
            team_name=team_name,
            analysis_type=AnalysisType.STATS,
            status=AnalysisStatus.PENDING,
        )
        
        analysis = self.repository.create(analysis)


        try:
            analysis.status = AnalysisStatus.RUNNING
            self.repository.update(analysis)

            result = self.agent.invoke(
                {
                    "messages":[
                        {
                            "role":"user",
                            "co"
                        }
                    ]
                }
            )

    async def scout_opposition(self, team_name: str, player_name: str, user_id: str) -> Analysis: 
        report = Scout_Report(
            team_name=team_name,
            player_name=player_name,
            status=AnalysisStatus.PENDING
        )
        report = self.repository.create(report)
        if report is None:
            raise ValueError
        
        

#need to add ability to 
    