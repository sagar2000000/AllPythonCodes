try:
  a=10
  b=0
  c=a/b
except:
  print('cant divide by zero')  

try:
  list=[1,2,4]
  print(list[4])
except IndexError :
  print("error index") 