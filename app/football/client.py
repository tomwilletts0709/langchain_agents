import httpx
from app.core.settings import settings

ENGLAND_TEAM_ID = 770
WORLD_CUP_CODE = "WC"


class FootballAPIClient:
    def __init__(self):
        self.base_url = settings.FOOTBALL_API_BASE_URL
        self.headers = {"X-Auth-Token": settings.FOOTBALL_STATS_API}

    def _get(self, path: str, params: dict = None) -> dict:
        with httpx.Client(headers=self.headers, timeout=10) as client:
            response = client.get(f"{self.base_url}{path}", params=params)
            response.raise_for_status()
            return response.json()

    # --- England squad ---
    def get_england_squad(self) -> dict:
        return self._get(f"/teams/{ENGLAND_TEAM_ID}")

    # --- England fixtures ---
    def get_england_matches(self, status: str = None) -> dict:
        params = {}
        if status:
            params["status"] = status  # SCHEDULED, LIVE, FINISHED
        return self._get(f"/teams/{ENGLAND_TEAM_ID}/matches", params=params)

    # --- World Cup competition ---
    def get_world_cup(self) -> dict:
        return self._get(f"/competitions/{WORLD_CUP_CODE}")

    def get_world_cup_matches(self, stage: str = None) -> dict:
        params = {}
        if stage:
            params["stage"] = stage  # GROUP_STAGE, ROUND_OF_16, QUARTER_FINALS, etc.
        return self._get(f"/competitions/{WORLD_CUP_CODE}/matches", params=params)

    def get_world_cup_teams(self) -> dict:
        return self._get(f"/competitions/{WORLD_CUP_CODE}/teams")

    def get_world_cup_standings(self) -> dict:
        return self._get(f"/competitions/{WORLD_CUP_CODE}/standings")

    def get_world_cup_scorers(self) -> dict:
        return self._get(f"/competitions/{WORLD_CUP_CODE}/scorers")

    # --- Specific match ---
    def get_match(self, match_id: int) -> dict:
        return self._get(f"/matches/{match_id}")

    # --- Specific team ---
    def get_team(self, team_id: int) -> dict:
        return self._get(f"/teams/{team_id}")

    def get_team_matches(self, team_id: int, status: str = None) -> dict:
        params = {}
        if status:
            params["status"] = status
        return self._get(f"/teams/{team_id}/matches", params=params)


football_client = FootballAPIClient()
