class Node:
    def __init__(self, name: str):
        self.name = name
    
    def __eq__(self, other) -> bool:
        if type(other) == Node:
            return self.name == other.name
        else:
            return self.name == other

    def __repr__(self) -> str:
        return self.name

class Path:
    def __init__(self, origin: Node, distance: int, destination: Node, initial_feromone: float):
        self.distance = distance
        self.origins = [origin, destination]
        self.feromone = initial_feromone
    
    def __repr__(self) -> str:
        return f"{self.origins[0]} <->[{self.distance}] {self.origins[1]}({self.feromone})"
    
    def __eq__(self, other) -> bool:
        return self.origins[0].name == other or self.origins[1].name == other
