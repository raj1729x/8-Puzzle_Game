from header import *

'''goal = [0,1,2,
           3,4,5,
           6,7,8]
Consider 0 as blank'''


x = Node([1,2,3,4,0,5,6,7,8])
x.explore()
print(x.search_space)
print(x.path_cost)






