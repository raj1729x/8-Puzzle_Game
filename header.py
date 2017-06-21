class Node:
    goal = [0,1,2,3,4,5,6,7,8]

    def __init__(self,initial_state):
        self.initial_state = initial_state
        self.search_space = []
        self.path_cost = []

    def Explore(self):
        blank = self.initial_state.index(0)
        #moves up
        if blank//3==1:
            temp2_state = self.initial_state[:]
            temp21 = temp2_state[blank]
            temp22 = temp2_state[blank-3]
            temp2_state[blank-3] = temp21
            temp2_state[blank] = temp22
            self.search_space.append(temp2_state)
        if blank//3==2:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank-3]
            temp_state[blank-3] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        #moves down
        if blank//3==0:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank+3]
            temp_state[blank+3] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        if blank//3==1:
            temp1_state = self.initial_state[:]
            temp11 = temp1_state[blank]
            temp12 = temp1_state[blank+3]
            temp1_state[blank+3] = temp11
            temp1_state[blank] = temp12
            self.search_space.append(temp1_state)
        #moves left
        if blank%3==1:
            temp2_state = self.initial_state[:]
            temp21 = temp2_state[blank]
            temp22 = temp2_state[blank-1]
            temp2_state[blank-1] = temp21
            temp2_state[blank] = temp22
            self.search_space.append(temp2_state)
        if blank%3==2:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank-1]
            temp_state[blank-1] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        #moves right
        if blank%3==0:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank+1]
            temp_state[blank+1] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)
        if blank%3==1:
            temp1_state = self.initial_state[:]
            temp11 = temp1_state[blank]
            temp12 = temp1_state[blank+1]
            temp1_state[blank+1] = temp11
            temp1_state[blank] = temp12
            self.search_space.append(temp1_state)
        #calculate cost for each path
        self.Cost()
 
    def Cost(self):
        for i in range(0,len(self.search_space)):
            cost = 0
            temp = self.search_space[i][:]
            for j in range(0,len(temp)):
                temp_val = temp[j]
                temp_ind = j
                goal_ind = self.goal.index(temp_val)
                cost = cost + abs((temp_ind%3)-(goal_ind%3)) + abs((temp_ind//3)-(goal_ind//3))
            self.path_cost.append(cost)                        
        
