from path import Path, Node
from ant import Ant
from random import choice
from collections import defaultdict
from tqdm import tqdm


class Map:
    def __init__(self, nodes: list[str], paths: list[Path], fi: float = 0.01):
        self.nodes = nodes
        self.paths = paths
        self.fi = fi

    def __repr__(self) -> str:
        return str(self.nodes) + '\n\n' + str(self.paths)

    def optimize(self, num_ants: int, num_iterations: int = 500) -> tuple[list[Node], int]:

        shortest_path = None
        min_length = 999999

        for iteration in tqdm(range(num_iterations)):
            Q = 10

            visited_paths = defaultdict(lambda: 0)

            for i in range(num_ants):
                sn = choice(self.nodes)
                ant = Ant(sn, self.paths[:], self.nodes[:])
                length, paths = ant.run()

                if length < min_length:

                    shortest_path = paths
                    min_length = length

                for path in paths:
                    visited_paths[path] += Q / length

            for i in range(len(self.paths)):
                self.paths[i].feromone = (
                    1 - self.fi) * self.paths[i].feromone + visited_paths[self.paths[i]]

            if iteration % 100 == 0:
                print(min_length)

        return shortest_path, length
