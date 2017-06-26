from header import *

initial_state = [1,2,3,4,0,5,6,7,8]
goal = [0,1,2,3,4,5,6,7,8]
explored = []
exp_mother = []
search = []
search_mother = [] 
#just to test if it works
search.append(initial_state)
search_mother.append(0)

#for BFS
while True:
    current_state = search[0]
    if(current_state == goal):
        explored.append(search[0])
        exp_mother.append(search_mother[0])
        break
    state = Node(current_state)
    state.Explore()
    for i in range(0,len(state.search_space)):
        if(state.search_space[i] not in explored):
            search.append(state.search_space[i])
            search_mother.append(len(explored))
    explored.append(search[0])
    exp_mother.append(search_mother[0])
    del search[0]
    del search_mother[0]

i=len(explored)-1
while True:
    print(explored[i])
    i=exp_mother[i]
    if explored[i] == initial_state:
        break
    

