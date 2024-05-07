import time

# def usingWhile():
#   i=0
#   while i<50000:
#     i=i+1
#     print(i)


# def usingFor():

#   for i in range(1,50001):
#     print(i)    



# init0=time.time()
# usingWhile()
# print(f" time is {time.time()-init0}")
# init1=time.time()
# usingFor()   
# print(f" time is {time.time()-init1}")


t=time.localtime()
formatted_time=time.strftime('%Y- %m-%d %H:%M:%S',t)
print(formatted_time)