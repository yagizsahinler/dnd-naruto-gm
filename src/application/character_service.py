from domain.character import Character
from typing import Dict


class CharacterService:

    VALID_STATS = {"STR", "DEX", "CON", "INT", "WIS", "CHA"}
    VALID_ELEMENTS = {"Fire", "Water", "Wind", "Earth", "Lightning"}
    VALID_CLANS = {"Uchiha", "Hyuga", "Haruno", "Nara", "Aburame", "Inuzuka"}  # genişletilebilir
    VALID_RANKS = {"Genin", "Chuunin", "Jounin", "ANBU", "Sannin"}

    @staticmethod
    def create_character(
        name: str,
        rank: str,
        clan: str,
        element: str,
        stats: Dict[str, int]
    ) -> Character:

        CharacterService.validate_inputs(rank, clan, element, stats)

        character = Character(
            name=name,
            rank=rank,
            clan=clan,
            element=element,
            stats=stats
        )
        return character

    @staticmethod
    def validate_inputs(rank: str, clan: str, element: str, stats: Dict[str, int]) -> None:
        if rank not in CharacterService.VALID_RANKS:
            raise ValueError(f"Geçersiz rank: {rank}")
        if clan not in CharacterService.VALID_CLANS:
            raise ValueError(f"Geçersiz klan: {clan}")
        if element not in CharacterService.VALID_ELEMENTS:
            raise ValueError(f"Geçersiz element: {element}")
        if set(stats.keys()) != CharacterService.VALID_STATS:
            raise ValueError(f"Stat anahtarları yanlış veya eksik: {stats.keys()}")
        for key, value in stats.items():
            if not (1 <= value <= 20):
                raise ValueError(f"{key} değeri 1-20 arasında olmalıdır (aldı: {value})")
