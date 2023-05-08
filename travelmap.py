from path import Path, Node

class Map:
    def __init__(self, paths: list[Path]):
        self.paths = paths
    
    def __repr__(self) -> str:
        return str(self.paths)
    
    def optimize(self) -> list[Node]:
        pass

