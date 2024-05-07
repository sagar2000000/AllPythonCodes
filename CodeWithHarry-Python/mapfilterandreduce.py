# #map
# def cube(x):
#   return x**3

# lisst=[1,2,3,4,5]
# newlist=list(map(cube,lisst))
# print(newlist)
# # or we can use lambda function as argument

# #filter
# def filter_function(a):
#   return a>3

# nl=list(filter(filter_function,lisst))
# print(nl)
from functools import reduce
l1=[1,2,3,4,5]
newl1=(reduce(lambda x,y:x+y,l1))
print(newl1)