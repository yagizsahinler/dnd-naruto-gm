import json
from domain.mission import Mission


class MissionRepository:
    @staticmethod
    def load_missions(path: str = "data/missions.json") -> list[Mission]:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Mission.from_dict(m) for m in data]

    @staticmethod
    def save_missions(missions: list[Mission], path: str = "data/missions.json") -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in missions], f, indent=2)
