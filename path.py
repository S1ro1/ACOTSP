class Node:
    def __init__(self, name: str):
        self.name = name

class Path:
    def __init__(self, origin: Node, distance: int, destination: Node):
        self.origin = origin
        self.distance = distance
        self.destination = destination
    
    def __repr__(self) -> str:
        return f"{self.origin.name} -> {self.destination.name}({self.distance})"
