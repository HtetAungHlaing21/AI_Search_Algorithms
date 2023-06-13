# A short report
'''
In Part-A, the .txt file is converted into a dictionary graph. It takes .txt file as input and returns the dictionary graph as output.
First, the node next to '#' is added to the temporary list, then is made unique. The index of each node in temporary list is checked whether even or odd.
If even, the node after it will be added to its list in the dictionary graph. If odd, the node before it will be added.

In Part-B, BFS algorithm is implemented. It takes the graph and initial node as inputs and returns the visited list (the order of exploration) as output.
Check every node that is connected to the initial node. If the node is not in visited list, add the node to both queue and visited.
Then, the first node of the queue is deleted. That allows to change the initial node in the next iteration. This will iterate as long as there are nodes left in the queue.

In Part-C, the graph, the initial node and the goal node are taken as inputs and the path from the initial node to goal node is returned as output.
First, the goal node will be initialized as current node. Check every node from the visited list from the beginning to the node before the current node.
If the node is connected to current node, add it to the front of the path list and break the loop. In the next iteration that node becomes the current node.
It will iterate as long as the goal node and current node are the same. Finally, the goal node is added to the end of the path list..
'''

# Import numpy library for unique function
import numpy as np
# Part-A (Reading the .txt file and extracting into a dictionary graph)
def graph(fileName):
    graph_dict = {} #An empty dictionary for the graph
    temp = [] #Temporary list for storing the nodes
    myFile = open(fileName, "r")  #Opening the file
    whole_text = myFile.readlines() #Read all and save it as a list
    for line in whole_text: #For every line in the text, the new line characters are removed first
        line.strip()
        for idx, char in enumerate(line): #For every character of that line
            if char == "#": #If the character is '#', the letter next to it will be added to the temporary list.
                temp.append(line[idx+1])
    for node in np.unique(temp): #The dictionary has keys of all unique nodes of temporary list and they all initialized as empty lists.
        graph_dict[node] = []
    for idx,node in enumerate(temp): #for every nodes in temporary list,
        if idx%2 == 0: #If the index of the node is even, the node after it will be added to its list in the dictionary.
            graph_dict[temp[idx]].append(temp[idx+1])
        else: #It it is odd, the node before it will be added to its list in the dictionary.
            graph_dict[temp[idx]].append(temp[idx-1])
    myFile.close()
    return graph_dict

# Part-B (BFS Implementation)
def BFS(graph, initial_node):
    queue = [] #Two empty lists for queue and visited
    visited = []
    queue.append(initial_node) #Initial node is added to both queue and visited.
    visited.append(initial_node)
    while len(queue) !=0 : #The loop will iterate as long as there are nodes in queue.
        initial_node = queue[0] #The first node from the queue will be assigned as the initial node.
        for node in graph[initial_node]: #For every node that is in connection with the initial node,
            if node not in visited: #if the node is not in visited list, add the node to both queue and visited.
                queue.append(node)
                visited.append(node)
        queue.pop(0) #Then, the first node of the queue is deleted.
    return visited

# Part-C (Finding the path)
def result(graph, initial_state, goal_state):
    visited = BFS(graph, initial_state) #The order of exploration
    path = [] #The empty list to store the path
    current_state = goal_state #Current node is initialized as goal node
    while current_state != initial_state:  #The loop will iterate as long as the current node is not initial node.
        index = visited.index(current_state) #The index of the current node in visited list
        for node in visited[:index]: #Check every node in visited from the beginning to the current node (but current node not included),
            if node in graph[current_state]: #If it is included in the connection of the current node, add to path list in the position of index 0.
                path.insert(0, node)
                current_state = node #Then, that node becomes the current node.
                break
    path.append(goal_state) #Finally, goal state is added at the end of the path list.
    return path

graph_dict = graph("Graph_info.txt")
print("Graph: ", graph_dict)
print("Order of exploring : ", BFS(graph_dict, "A"))
print("Path : ", result(graph_dict, "A", "F"))