from dataclasses import dataclass, field
from typing import Dict, List
import random


@dataclass
class Character:
    name: str
    rank: str
    clan: str
    element: str
    level: int = 1
    exp: int = 0
    jp: int = 0  # 🆕 Jutsu Point
    stats: Dict[str, int] = field(default_factory=lambda: {
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHA": 10
    })
    learned_jutsus: List[str] = field(default_factory=list)
    hp: int = field(init=False)
    cp: int = field(init=False)

    def __post_init__(self):
        self.hp = self.calculate_hp()
        self.cp = self.calculate_cp()

    def get_modifier(self, stat_value: int) -> int:
        return (stat_value - 10) // 2

    def calculate_cp(self) -> int:
        con_mod = self.get_modifier(self.stats["CON"])
        wis_mod = self.get_modifier(self.stats["WIS"])
        return 10 + con_mod + wis_mod + (self.level * 2)

    def calculate_hp(self) -> int:
        base_hp = 20
        con_mod = self.get_modifier(self.stats["CON"])
        return base_hp + (self.level - 1) * (5 + con_mod)

    def add_exp(self, amount: int) -> None:
        self.exp += amount
        while self.exp >= self.level * 300:
            self.level_up()

    def level_up(self) -> None:
        self.level += 1
        self.jp += 1
        self.hp = self.calculate_hp()
        self.cp = self.calculate_cp()
        print(f"🎉 {self.name} seviye atladı! Yeni seviye: {self.level} | Yeni JP: {self.jp}")

    def short_rest(self) -> int:
        wis_mod = self.get_modifier(self.stats["WIS"])
        recovered = random.randint(1, 6) + wis_mod
        recovered = max(1, recovered)
        self.cp = min(self.cp + recovered, self.calculate_cp())
        return recovered

    def long_rest(self) -> None:
        self.cp = self.calculate_cp()

    def learn_jutsu(self, jutsu_name: str, cost: int = 1) -> bool:
        if self.jp >= cost and jutsu_name not in self.learned_jutsus:
            self.jp -= cost
            self.learned_jutsus.append(jutsu_name)
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "rank": self.rank,
            "clan": self.clan,
            "element": self.element,
            "level": self.level,
            "exp": self.exp,
            "jp": self.jp,
            "stats": self.stats,
            "learned_jutsus": self.learned_jutsus
        }

    @staticmethod
    def from_dict(data: dict) -> "Character":
        return Character(
            name=data["name"],
            rank=data["rank"],
            clan=data["clan"],
            element=data["element"],
            level=data.get("level", 1),
            exp=data.get("exp", 0),
            jp=data.get("jp", 0),
            stats=data.get("stats", {
                "STR": 10,
                "DEX": 10,
                "CON": 10,
                "INT": 10,
                "WIS": 10,
                "CHA": 10
            }),
            learned_jutsus=data.get("learned_jutsus", [])
        )
