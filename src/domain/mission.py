from dataclasses import dataclass


@dataclass
class Mission:
    id: int
    title: str
    description: str
    rank: str  # D, C, B, A, S
    exp_reward: int
    is_completed: bool = False

    def complete(self):
        """Görevi tamamlar ve tamamlandı olarak işaretler."""
        self.is_completed = True

    def __str__(self):
        status = "✅" if self.is_completed else "🕓"
        return f"{status} [{self.rank}-Rank] {self.title} (EXP: {self.exp_reward})"
