import graph_data
import global_game_data
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


def get_random_path():
    return [1,2]


def get_dfs_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_index = 0

    vertex_Stack = []
    visited_Set = set()
    dfs_path = []

    # Push starting vertex to vertex stack
    vertex_Stack.append(start_index)

    while vertex_Stack:
        current_vertex = vertex_Stack.pop()

        if current_vertex not in visited_Set:
            visited_Set.add(current_vertex)
            dfs_path.append(current_vertex)

            for neighbor in current_graph[current_vertex][1]:
                if neighbor not in visited_Set:
                    vertex_Stack.append(neighbor)

    return dfs_path





    

    # graph_data[a] = gives you graph at index a
    # graph_data[a][0] = start node of graph a
    # graph_data[a][length-1] = exit node of graph a
    # graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
    # graph_data[a][b][1] = adjacency list of point b in graph a
    # Only the start and exit nodes are dead ends (all other nodes have degree >= 2)

    # vertexStack.append(startVertex)










    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
