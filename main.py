from travelmap import Map
from utils import parse_input

if __name__ == "__main__":
    prob = parse_input("examples/1.txt")
    m = Map(*prob)
    m.optimize(25)

