from dataclasses import dataclass


@dataclass
class Mission:
    id: int
    title: str
    description: str
    rank: str  # D, C, B, A, S
    exp_reward: int
    location: str
    previous_context: str = ""
    is_completed: bool = False

    def complete(self):
        """Görevi tamamlar ve tamamlandı olarak işaretler."""
        self.is_completed = True

    def __str__(self):
        status = "✅" if self.is_completed else "🕓"
        return f"{status} [{self.rank}-Rank] {self.title} in {self.location} (EXP: {self.exp_reward})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "rank": self.rank,
            "exp_reward": self.exp_reward,
            "location": self.location,
            "previous_context": self.previous_context,
            "is_completed": self.is_completed
        }

    @staticmethod
    def from_dict(data: dict) -> "Mission":
        return Mission(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            rank=data["rank"],
            exp_reward=data["exp_reward"],
            location=data["location"],
            previous_context=data.get("previous_context", ""),
            is_completed=data.get("is_completed", False)
        )
