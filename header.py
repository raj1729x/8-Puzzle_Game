"""goal = [0,1,2,
        3,4,5,
        6,7,8]
Consider 0 as blank"""

class Node:
    goal = [0,1,2,3,4,5,6,7,8]

    def __init__(self,initial_state):
        self.initial_state = initial_state
        self.search_space = []
        
    def explore(self):
        blank = self.initial_state.index(0)
        print(blank)
        #this does horizontal movements of blank
        if blank%3==0:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank+1]
            temp_state[blank+1] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)

        if blank%3==2:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank-1]
            temp_state[blank-1] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)

        if blank%3==1:
            temp1_state = self.initial_state[:]
            temp11 = temp1_state[blank]
            temp12 = temp1_state[blank+1]
            temp1_state[blank+1] = temp11
            temp1_state[blank] = temp12
            self.search_space.append(temp1_state)

            temp2_state = self.initial_state[:]
            temp21 = temp2_state[blank]
            temp22 = temp2_state[blank-1]
            temp2_state[blank-1] = temp21
            temp2_state[blank] = temp22
            self.search_space.append(temp2_state)
    
        #this does verticle movements
        if blank//3==0:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank+3]
            temp_state[blank+3] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)

        if blank//3==2:
            temp_state = self.initial_state[:]
            temp1 = temp_state[blank]
            temp2 = temp_state[blank-3]
            temp_state[blank-3] = temp1
            temp_state[blank] = temp2
            self.search_space.append(temp_state)

        if blank//3==1:
            temp1_state = self.initial_state[:]
            temp11 = temp1_state[blank]
            temp12 = temp1_state[blank+3]
            temp1_state[blank+3] = temp11
            temp1_state[blank] = temp12
            self.search_space.append(temp1_state)

            temp2_state = self.initial_state
            temp21 = temp2_state[blank]
            temp22 = temp2_state[blank-3]
            temp2_state[blank-3] = temp21
            temp2_state[blank] = temp22
            self.search_space.append(temp2_state)

 
