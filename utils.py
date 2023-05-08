from path import Path, Node

def parse_input(file_path: str) -> tuple[list[str], list[Path]]:
    with open(file_path, 'r') as f:
        paths = f.readlines()
    
    paths = [p.strip() for p in paths]
    
    res = []
    node_set = set()
    gotten_paths = []

    for p in paths:
        v = p.split(' ')
        node_set.add(v[0])
        node_set.add(v[2])
        if tuple(sorted((v[0], v[2]))) in gotten_paths:
            continue   
        v[0] = Node(v[0])
        v[1] = int(v[1])
        v[2] = Node(v[2])
        res.append(Path(*v, 1/len(paths)))
    
    return list(node_set), res
    


    
