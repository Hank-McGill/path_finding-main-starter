import graph_data
import global_game_data
from collections import deque
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_segment_path_random(graph, start, goal):
    # Edge case: start and goal are the same
    if start == goal:
        return [start]

    # Try to walk random path to goa without hitting dead end
    while True:
        current_node = start
        path = [start]
        visited = {start}

        while current_node != goal:
            # Only look at adjacent nodes not yet visited in segment
            unvisited_adjacent_nodes = []
            for adjacent_node in graph[current_node][1]:
                if adjacent_node not in visited:
                    unvisited_adjacent_nodes.append(adjacent_node)

            # If hit dead end, restart
            if not unvisited_adjacent_nodes:
                break

            # Pick random unvisited adjacent node
            next_node = random.choice(unvisited_adjacent_nodes)
            visited.add(next_node)
            path.append(next_node)
            current_node = next_node

        if current_node == goal:
            return path
        

def get_random_path():
    # Initialize graph, start, target, end
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(current_graph) - 1

    # Get individual paths
    path_to_target = get_segment_path_random(current_graph, start, target)
    path_to_end = get_segment_path_random(current_graph, target, end)

    # Remove the duplicate target node from path_2
    return path_to_target + path_to_end[1:]


def get_segment_path_dfs(graph, start, goal):
    # Edge case: start and goal are the same
    if start == goal:
        return [start]

    # Initialize stack for dfs search traversal
    node_stack = [start]
    visited_set = set()
    parent_map = {}

    while node_stack:
        current_node = node_stack.pop()

        # Build path from back to start then reverse
        if current_node == goal:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = parent_map[current_node]
            path.append(start)
            path.reverse()
            return path

        # Process node if not visited yet
        if current_node not in visited_set:
            visited_set.add(current_node)

            # Add adjacent nodes to visited and parent set if needed
            for adjacent_node in graph[current_node][1]:
                if adjacent_node not in visited_set:
                    node_stack.append(adjacent_node)
                    if adjacent_node not in parent_map:
                        parent_map[adjacent_node] = current_node

    # Return empty list if no valid paths
    return []


def get_dfs_path():
    # Initialize graph, start, target, end
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(current_graph) - 1

    # Get individual paths
    path_to_target = get_segment_path_dfs(current_graph, start, target)
    path_to_end = get_segment_path_dfs(current_graph, target, end)

    # Remove the duplicate target node from path_2
    return path_to_target + path_to_end[1:]
    

def get_segment_path_bfs(graph, start, goal):
    # Edge case: start and goal are the same
    if start == goal:
        return [start]

    # Initialize stack for bfs search traversal
    node_queue = deque([start])
    visited_set = {start}
    parent_map = {}
    
    while node_queue:
        current_node = node_queue.popleft()

        # Build path from back to start then reverse
        if current_node == goal:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = parent_map[current_node]
            path.append(start)
            path.reverse()
            return path

        # Check for adjacent_nodes
        for adjacent_node in graph[current_node][1]:
            # Process adjacent nodes if not yet visited
            if adjacent_node not in visited_set:
                visited_set.add(adjacent_node)
                parent_map[adjacent_node] = current_node
                node_queue.append(adjacent_node)

    # Return empty list if no valid paths
    return []


def get_bfs_path():
    # Initialize graph, start, target, end
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(current_graph) - 1

    # Get individual paths
    path_to_target = get_segment_path_bfs(current_graph, start, target)
    path_to_end = get_segment_path_bfs(current_graph, target, end)


    # Remove the duplicate target node from path_2
    return path_to_target + path_to_end[1:]


def get_dijkstra_path():
    return [1,2]


def verify_postconditions(path, graph, target, goal):
    # Postcondition a: Result path includes target node
    assert target in path, f"Target node {target} is missing from the path"
    
    # Postcondition b: Result path ends at goal node
    assert path[-1] == goal, f"Path ends at {path[-1]}, expected goal node {goal}"
    
    # Postcondition c: Every pair of sequential vertices in the path are connected by an edge
    for i in range(len(path) - 1):
        first_node = path[i]
        next_node = path[i + 1]
        assert next_node in graph[first_node][1], f"No edge exists between node {first_node} and node {next_node}."