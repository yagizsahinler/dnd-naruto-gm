from domain.character import Character
from domain.mission import Mission


class MissionService:

    @staticmethod
    def list_available_missions(missions: list[Mission]) -> list[Mission]:
        return [m for m in missions if not m.is_completed]

    @staticmethod
    def complete_mission(character: Character, mission: Mission) -> str:
        if mission.is_completed:
            return f"⚠️ Bu görev zaten tamamlanmış: {mission.title}"

        mission.complete()
        character.add_exp(mission.exp_reward)

        return f"""
🎯 Görev Tamamlandı: {mission.title}
+{mission.exp_reward} EXP kazanıldı!
Yeni EXP: {character.exp}
Seviye: {character.level} | CP: {character.cp} | HP: {character.hp}
"""
