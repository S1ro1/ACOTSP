from travelmap import Map
from utils import parse_input

if __name__ == "__main__":
    paths = parse_input("examples/1.txt")
    m = Map(paths)
    print(m)




