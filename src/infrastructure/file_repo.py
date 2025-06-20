import json
import os
from typing import Optional
from domain.character import Character
from domain.jutsu import Jutsu
from domain.mission import Mission


class CharacterFileRepository:

    DATA_DIR = "data"
    CHARACTER_FILE = os.path.join(DATA_DIR, "character.json")

    @staticmethod
    def save_character(character: Character) -> None:
        os.makedirs(CharacterFileRepository.DATA_DIR, exist_ok=True)
        data = {
            "name": character.name,
            "rank": character.rank,
            "clan": character.clan,
            "element": character.element,
            "level": character.level,
            "exp": character.exp,
            "jp": character.jp,  # 🆕 JP kaydı
            "stats": character.stats,
            "learned_jutsus": character.learned_jutsus
        }
        with open(CharacterFileRepository.CHARACTER_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Karakter dosyaya kaydedildi: {CharacterFileRepository.CHARACTER_FILE}")

    @staticmethod
    def load_character() -> Optional[Character]:
        if not os.path.exists(CharacterFileRepository.CHARACTER_FILE):
            print("❌ Karakter dosyası bulunamadı.")
            return None

        with open(CharacterFileRepository.CHARACTER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        try:
            character = Character(
                name=data["name"],
                rank=data["rank"],
                clan=data["clan"],
                element=data["element"],
                level=data.get("level", 1),
                exp=data.get("exp", 0),
                jp=data.get("jp", 0),  # 🆕 JP yüklemesi
                stats=data["stats"],
                learned_jutsus=data.get("learned_jutsus", [])
            )
            print(f"📂 Karakter yüklendi: {character.name} (Seviye {character.level})")
            return character
        except KeyError as e:
            print(f"🚫 Hatalı veri formatı: {e}")
            return None

    @staticmethod
    def load_jutsus(file_path: str = "data/jutsus.json") -> list[Jutsu]:
        if not os.path.exists(file_path):
            print(f"❌ Jutsu dosyası bulunamadı: {file_path}")
            return []

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        jutsus = []
        for entry in data:
            try:
                jutsu = Jutsu(
                    name=entry["name"],
                    jutsu_type=entry["jutsu_type"],
                    cp_cost=entry["cp_cost"],
                    damage_dice=entry["damage_dice"],
                    description=entry.get("description", ""),
                    uses=entry.get("uses", 0)
                )
                jutsus.append(jutsu)
            except KeyError as e:
                print(f"🚫 Hatalı jutsu verisi: {e}")
        return jutsus

    @staticmethod
    def load_missions(file_path: str = "data/missions.json") -> list[Mission]:
        if not os.path.exists(file_path):
            print(f"❌ Görev dosyası bulunamadı: {file_path}")
            return []

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        missions = []
        for entry in data:
            try:
                mission = Mission(
                    id=entry["id"],
                    title=entry["title"],
                    description=entry["description"],
                    rank=entry["rank"],
                    exp_reward=entry["exp_reward"],
                    is_completed=entry.get("is_completed", False)
                )
                missions.append(mission)
            except KeyError as e:
                print(f"🚫 Hatalı görev verisi: {e}")
        return missions
