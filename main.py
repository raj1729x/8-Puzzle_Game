from header import *

initial_state = [1,2,3,4,0,5,6,7,8]
goal = [0,1,2,3,4,5,6,7,8]
explored = []
search = []

#just to test if it works
search.append(initial_state)

#for BFS
while True:
    current_state = search[0]
    print(current_state)
    if(current_state == goal):
        break
    state = Node(current_state)
    state.Explore()
    for i in range(0,len(state.search_space)):
        if(state.search_space[i] not in explored):
            search.append(state.search_space[i])
    explored.append(current_state)
    search.remove(current_state)
    
    

