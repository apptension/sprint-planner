from dataclasses import dataclass


@dataclass(frozen=True)
class Issue:
    id: str
    name: str
    estimation: int = 1
    priority: int = 0

    def __str__(self):
        return "{} | priority: {} | estimation: {}".format(
            self.name, self.priority, self.estimation
        )
