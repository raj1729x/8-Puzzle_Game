goal = [0,1,2,3,4,5,6,7,8]
explored = []
exp_mother = []
search = []
search_mother = []
path_cost = []

max_depth = [0]
algorithm_used = ""

class Node:
    
    def __init__(self,current_node,current_node_mother_ind):
        self.search_space = []
        self.path_cost = []
        self.current_node = current_node
        i = current_node_mother_ind
        depth = 0
        while True:
            if current_node_mother_ind == -1:
                self.current_node_mother = current_node_mother_ind
                self.current_node_mother_ind = current_node_mother_ind
                self.depth = 0
                break
            else:
                self.current_node_mother = exp_mother[current_node_mother_ind]
                self.current_node_mother_ind = current_node_mother_ind
                depth = depth + 1
                if exp_mother[i] == -1 :
                    break
                i = exp_mother[i]
        self.depth = depth
        
    def Explore(self):
        explored.append(self.current_node)
        exp_mother.append(self.current_node_mother_ind)
        if self.depth > max_depth[0] :
            max_depth[0] = self.depth
        
        blank = self.current_node.index(0)
        #moves up
        if blank//3==1:
            temp2_state = self.current_node[:]
            temp21 = temp2_state[blank]
            temp22 = temp2_state[blank-3]
            temp2_state[blank-3] = temp21
            temp2_state[blank] = temp22
            self.search_space.append(temp2_state)
        if blank//3==2:
            temp_state = self.current_node[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank-3]
            temp_state[blank-3] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        #moves down
        if blank//3==0:
            temp_state = self.current_node[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank+3]
            temp_state[blank+3] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        if blank//3==1:
            temp1_state = self.current_node[:]
            temp11 = temp1_state[blank]
            temp12 = temp1_state[blank+3]
            temp1_state[blank+3] = temp11
            temp1_state[blank] = temp12
            self.search_space.append(temp1_state)
        #moves left
        if blank%3==1:
            temp2_state = self.current_node[:]
            temp21 = temp2_state[blank]
            temp22 = temp2_state[blank-1]
            temp2_state[blank-1] = temp21
            temp2_state[blank] = temp22
            self.search_space.append(temp2_state)
        if blank%3==2:
            temp_state = self.current_node[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank-1]
            temp_state[blank-1] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        #moves right
        if blank%3==0:
            temp_state = self.current_node[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank+1]
            temp_state[blank+1] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        if blank%3==1:
            temp1_state = self.current_node[:]
            temp11 = temp1_state[blank]
            temp12 = temp1_state[blank+1]
            temp1_state[blank+1] = temp11
            temp1_state[blank] = temp12
            self.search_space.append(temp1_state)
        #calculate cost for each path
        
    def Cost(self):
        for i in range(0,len(self.search_space)):
            cost = 0
            temp = self.search_space[i][:]
            for j in range(0,len(temp)):
                temp_val = temp[j]
                temp_ind = j
                goal_ind = goal.index(temp_val)
                cost = cost + abs((temp_ind%3)-(goal_ind%3)) + abs((temp_ind//3)-(goal_ind//3))
            self.path_cost.append(cost)                        
        
