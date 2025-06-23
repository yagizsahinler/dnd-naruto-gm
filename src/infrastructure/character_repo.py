import json
from domain.character import Character


class CharacterRepository:
    @staticmethod
    def load_character(path: str) -> Character:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Character.from_dict(data)

    @staticmethod
    def save_character(character: Character, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(character.to_dict(), f, indent=2)
