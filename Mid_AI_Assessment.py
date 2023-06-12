import numpy as np
# Part-A (Graph)
def graph(fileName):
    graph_dict = {}
    temp = []
    myFile = open(fileName, "r")
    whole_text = myFile.readlines()
    for line in whole_text:
        line.strip()
        for idx, char in enumerate(line):
            if char == "#":
                temp.append(line[idx+1])
    for node in np.unique(temp):
        graph_dict[node] = []
    for idx,node in enumerate(temp):
        if idx%2 == 0:
            graph_dict[temp[idx]].append(temp[idx+1])
        else:
            graph_dict[temp[idx]].append(temp[idx-1])
    myFile.close()
    return graph_dict

# Part-B (BFS)
def BFS(graph, initial_node):
    queue = []
    visited = []
    queue.append(initial_node)
    visited.append(initial_node)
    while len(queue) !=0 :
        initial_node = queue[0]
        for item in graph[initial_node]:
            if item not in visited:
                queue.append(item)
                visited.append(item)
        queue.pop(0)
    return visited


# Part-C

def result(graph, initial_state, goal_state):
    visited = BFS(graph, initial_state)
    path = []
    current_state = goal_state
    while current_state != initial_state:
        index = visited.index(current_state)
        for node in visited[:index]:
            if node in graph[current_state]:
                path.insert(0, node)
                current_state = node
                break
    path.append(goal_state)
    return path

graph_dict = graph("Graph_info.txt")
print("Graph: ", graph_dict)
print("Order of exploring : ", BFS(graph_dict, "A"))
print("Path : ", result(graph_dict, "A", "F"))