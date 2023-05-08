from path import Path, Node
import numpy as np


class Ant:
    def __init__(self, starting_node: str, map_copy: list[Path], nodes: list[str], alpha: float = 0.9, beta: float = 1.5):
        self.visited: list[str] = []
        self.starting_node: str = starting_node
        self.map: list[Path] = map_copy
        self.alpha = alpha
        self.beta = beta
        self.all_nodes = nodes

    def run(self):
        res = []
        node = self.starting_node
        self.visited.append(node)

        for i in range(0, len(self.all_nodes)):

            if i == len(self.all_nodes) - 1:
                possible_paths = [p for p in self.map if p.contains(
                    node) and p.contains(self.starting_node)]
            else:
                possible_paths = [p for p in self.map if p.contains(
                    node) and any(n not in self.visited for n in p.origins)]

            desirabilities = [1/p.distance for p in possible_paths]

            products = [p.feromone ** self.alpha * d **
                        self.beta for p, d in zip(possible_paths, desirabilities)]
                

            probs = [p / sum(products) for p in products]
            path = possible_paths[np.random.multinomial(
                1, probs, size=1).argmax()]

            node = path.origins[1] if path.origins[1] != node else path.origins[0]
            res.append(path)

            self.visited.append(node.name)

        total_length = sum([p.distance for p in res])

        return total_length, res
