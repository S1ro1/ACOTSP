from travelmap import Map
from utils import parse_input

if __name__ == "__main__":

    # 7293
    prob = parse_input("examples/3.txt")
    print(len(prob[0]), len(prob[1]))
    m = Map(*prob)
    path, length = m.optimize(1, num_iterations=2000)
    print(length)
    print(path)
