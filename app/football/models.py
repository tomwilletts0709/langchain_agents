from sqlmodels import SQLModel, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum
import UUID
from app.agents._common import AgentBase

class PlayerStats(SQLModel, table=True, schema="analyst"): 
    id: UUID
    api_id: int
    player_name: str
    goals_scored: int
    assists: int
    overall_performance: str
    expected_goals: Optional[float] = None
    expected_assists: Optional[float] = None
    passes_completed: Optional[int] = None
    pass_accuracy: Optional[float] = None
    aerial_duels_won: Optional[int] = None
    duel_wons: Optional[int] = None
    interceptions: Optional[int] = None
    shots_on_target: Optional[int] = None
    shot_accuracy: Optional[float] = None
    fouls_committed: Optional[int] = None
    fouls_suffered: Optional[int] = None
    yellow_cards: Optional[int] = None
    red_cards: Optional[int] = None
    offside: Optional[int] = None
    penatlies_scored: Optional[int] = None
    penatlies_missed: Optional[int] = None
    minutes_played: Optional[int] = None
    matches_played: Optional[int] = None
    position: Optional[str] = None
    team: Optional[str] = None

class TeamStats(SQLModel, table=True, schema="analyst"):
    id: UUID
    api_id: int
    team_name: str
    matches_played: int
    wins: int
    losses: int
    draws: int
    goals_scored: int
    goals_conceded: int
    clean_sheets: Optional[int] = None
    possession_percentage: Optional[float] = None
    pass_accuracy: Optional[float] = None
    shots_on_target_per_game: Optional[float] = None
    tackles_per_game: Optional[float] = None
    expected_goals_per_game: Optional[float] = None
    expected_goals_conceded_per_game: Optional[float] = None
    interceptions_per_game: Optional[float] = None
    fouls_committed_per_game: Optional[float] = None
    fouls_suffered_per_game: Optional[float] = None
    yellow_cards_per_game: Optional[float] = None
    red_cards_per_game: Optional[float] = None
    offside_per_game: Optional[float] = None
    average_goals_scored_per_game: Optional[float] = None
    average_goals_conceded_per_game: Optional[float] = None
    table_position: Optional[int] = None
    recent_form: Optional[str] = None
    next_opposition: Optional[str] = None
    qualify_from_group_stage: Optional[bool] = None

class MatchAnalysis(SQLModel, table=True, schema="analyst"):
    id: UUID
    match_id: int
    key_moments: List[str]
    player_performances: List[str]
    tactical_insights: List[str]