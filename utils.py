def parse_input(file_path: str) -> list[Path]:
    with open(file_path, 'r') as f:
        paths = f.readlines()
    
    paths = [p.strip() for p in paths]
    
    res = []
    for p in paths:
        v = p.split(' ')
        v[0] = Node(v[0])
        v[1] = int(v[1])
        v[2] = Node(v[2])
        res.append(Path(*v))
        res.append(Path(*v[::-1]))
    
    return res
