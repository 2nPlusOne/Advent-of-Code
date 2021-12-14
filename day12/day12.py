from os import path

def main():
    with open(path.join(path.dirname(__file__), 'sample.txt')) as f:
        lines = [line.strip().split("-") for line in f.readlines()]
    f.close()

    graph = create_graph_from_input(lines)
    
    part1_paths = BFS_traversals_part1(graph)
    part2_paths = BFS_traversals_part2(graph)
    print(f"Part 1: The number of paths through the cave system that visit small caves at least once is {len(part1_paths)}.")
    print(f"Part 2: The number of paths through the cave system that visit a single small cave twice and the rest once is {len(part2_paths)}.")

def create_graph_from_input(lines):
    graph = {}
    for line in lines:
        if line[0] not in graph:
            graph[line[0]] = []
        if line[1] not in graph:
            graph[line[1]] = []
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    return graph

def BFS_traversals_part1(graph: dict, start = 'start', end = 'end') -> list:
    """Returns a list of all unique paths through the cave system from start to end, visiting each small cave at most once."""
    queue = [[start]] # List of paths left to explore, initialized to the start node
    paths = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        neighbors = graph[node]
        if node == end: # Found a path to the end
            paths.append(path) # Add the path to the list of paths
            continue
        for neighbor in neighbors:
            if neighbor not in path or neighbor.isupper():
                queue.append(path + [neighbor]) # Add the new path branch to the queue
    return paths

def BFS_traversals_part2(graph: dict, start = 'start', end = 'end') -> list:
    """Returns a list of all unique paths through the cave system from start to end, visiting a single small cave at most twice, and the rest once."""
    queue = [([start], False)] # A list of paths and whether or not the path has yet to visit a single small cave twice
    paths = []
    while queue:
        path, small_revisited = queue.pop(0)
        node = path[-1]
        neighbors = graph[node]

        if node == end:
            paths.append(path)
            continue
        for neighbor in neighbors: 
            if neighbor not in path or neighbor.isupper():
                queue.append((path + [neighbor], small_revisited))
            elif not small_revisited and neighbor != 'start':
                queue.append((path + [neighbor], True))
    return paths


if __name__ == '__main__':
    main()