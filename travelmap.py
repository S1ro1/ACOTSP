from path import Path, Node
from ant import Ant
from random import choice

class Map:
    def __init__(self, nodes: list[str], paths: list[Path]):
        self.nodes = nodes
        self.paths = paths
    
    def __repr__(self) -> str:
        return str(self.nodes) + '\n\n' + str(self.paths)
    
    def optimize(self, num_ants: int) -> list[Node]:
        for i in range(num_ants):
            sn = choice(self.nodes)
            ant = Ant(sn, self.paths[:], self.nodes[:])
            paths = ant.run()
        
        print(sn)
        print(paths)
        


        


