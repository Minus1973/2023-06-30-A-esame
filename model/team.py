from dataclasses import dataclass
#per crearlo devo usare TUTTI i campi del db, anche quelli che non usero
@dataclass
class Team:
    teamCode: str
    name: str
    ID: int
    totSalary: float

    #hash con la chiave
    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"{self.teamCode} ({self.name})"