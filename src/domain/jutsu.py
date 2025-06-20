from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Jutsu:
    name: str
    jutsu_type: Literal["Taijutsu", "Ninjutsu", "Genjutsu", "Temel"]
    cp_cost: int
    damage_dice: str  # örn: "1d8"
    description: str = ""
    uses: int = 0  # kaç kez kullanıldı

    def use(self) -> None:
        """Jutsu bir kez kullanıldığında çağrılır."""
        self.uses += 1

    def is_evolved(self) -> bool:
        """Jutsu'nun evrimleşip evrimleşmediğini döner (örnek eşik: 3 kullanım)"""
        return self.uses >= 3

    def __str__(self) -> str:
        evo = " (Evrimleşmiş)" if self.is_evolved() else ""
        return f"{self.name} [{self.jutsu_type}] - CP: {self.cp_cost}, Zarar: {self.damage_dice}{evo}"
