from travelmap import Map
from utils import parse_input, pprint_path
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('-i', '--input-file', required=True,
                        help='Path to file with graph')
    parser.add_argument('--num-ants', default=25, type=int,
                        help='Number of ants to run optimization with')
    parser.add_argument('--num-iterations', default=500, type=int,
                        help='Number of iterations to run optimization for')

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    graph = parse_input(args.input_file)
    m = Map(*graph)
    path, shortest_distance = m.optimize(
        num_ants=args.num_ants, num_iterations=args.num_iterations)
    pprint_path(path)
    print(f"{shortest_distance=}")


if __name__ == "__main__":
    main()
