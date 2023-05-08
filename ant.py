from path import Path, Node
import numpy as np

class Ant:
    def __init__(self, starting_node: str, map_copy: list[Path], nodes: list[str], alpha: float = -0.1, beta: float = 1.05):
        self.visited: list[str] = []
        self.starting_node: str = starting_node
        self.map: list[Path] = map_copy
        self.alpha = alpha
        self.beta = beta
        self.all_nodes = nodes

    def run(self):
        self.visited.append(self.starting_node)

        res = []
        node = self.starting_node
        while len(self.visited) != len(self.all_nodes):
            possible_paths = [p for p in self.map if p == node and p.origins[0].name]
            possible_paths = [p for p in possible_paths if not (p.origins[0] == node and p.origins[1] in self.visited or p.origins[1] == node and p.origins[0] in self.visited)]

            desirabilities = [1/p.distance for p in possible_paths]

            products = [p.feromone ** self.alpha * d ** self.beta for p, d in zip(possible_paths, desirabilities)]

            probs = [p / sum(products) for p in products]
            path = possible_paths[np.random.multinomial(1, probs, size=1).argmax()]

            node = path.origins[1] if path.origins[1] != node else path.origins[0]
            self.visited.append(node)
            res.append(path)
        
        total_length = sum([p.distance for p in res])
        print(total_length)
        
        return res






