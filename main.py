#initial_state = [1,4,2,3,7,5,6,8,0]
#initial_state = [5,0,2,3,1,4,6,7,8]
initial_state = [1,2,3,4,5,0,6,7,8]

from header import *
import time

#just to test if it works
search.append(initial_state)
search_mother.append(-1)

def BFS():
    global algorithm_used
    algorithm_used = "BSF"
    while True:
        state = Node(search[0],search_mother[0])
        if(state.current_node == goal):
            explored.append(search[0])
            exp_mother.append(search_mother[0])
            break
        state.Explore()
        for i in range(0,len(state.search_space)):
            if(state.search_space[i] not in explored):
                search.append(state.search_space[i])
                search_mother.append(len(explored)-1)
        del search[0]
        del search_mother[0]

def DFS(maxdepth):
    global algorithm_used
    algorithm_used = "DSF"
    while True:
        if len(search) == 0:
            print("Cannot find answer in this small depth")
            break
        state = Node(search[len(search)-1],search_mother[len(search_mother)-1])
        if state.depth == maxdepth :
            del search[len(search)-1]
            del search_mother[len(search_mother)-1]
            continue
        if(state.current_node == goal):
            explored.append(search[len(search)-1])
            exp_mother.append(search_mother[len(search)-1])
            break
        state.Explore()
        del search[len(search)-1]
        del search_mother[len(search_mother)-1]
        for i in range(0,len(state.search_space)):
            if(state.search_space[i] not in explored):
                search.append(state.search_space[i])
                search_mother.append(len(explored)-1)

def UCS():
    global algorithm_used
    algorithm_used = "UCS"
    cost = 0
    temp = search[0][:]
    for j in range(0,len(temp)):
        temp_val = temp[j]
        temp_ind = j
        goal_ind = goal.index(temp_val)
        cost = cost + abs((temp_ind%3)-(goal_ind%3)) + abs((temp_ind//3)-(goal_ind//3))
    path_cost.append(cost)

    while True:
        state = Node(search[0],search_mother[0])
        if(state.current_node == goal):
            explored.append(search[0])
            exp_mother.append(search_mother[0])
            break
        state.Explore()
        state.Cost()
        for i in range(0,len(state.search_space)):
            if(state.search_space[i] not in explored):
                search.append(state.search_space[i])
                path_cost.append(state.path_cost[i])
                search_mother.append(len(explored)-1)
        del search[0]
        del search_mother[0]
        del path_cost[0]
        for i in range(0,len(path_cost)-1):
            for j in range(i,len(path_cost)):
                if path_cost[i] > path_cost[j]:
                    temp1 = path_cost[i]
                    temp2 = path_cost[j]
                    path_cost[i] = temp2
                    path_cost[j] = temp1
                    temp1 = search[i]
                    temp2 = search[j]
                    search[i] = temp2
                    search[j] = temp1
                    temp1 = search_mother[i]
                    temp2 = search_mother[j]
                    search_mother[i] = temp2
                    search_mother[j] = temp1
                    
start_time = time.time()
        
#UCS()       
#DFS(10)
BFS()

elapse_time = time.time() - start_time

print("Algorithm Used : " + str(algorithm_used))
print("Number of Nodes explored : " + str(len(explored)))
print("Maximum Depth Explored : " + str(max_depth[0]))
print("Time required : " + str(elapse_time) + " seconds")
print("Steps :")
i=len(explored)-1
while True:
    print(explored[i])
    if explored[i] == initial_state:
        break
    i=exp_mother[i]
    
