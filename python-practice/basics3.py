message=input("Enter your message here")
# for index,i in enumerate(message):
#   if(index%2==0):
#     print(i)
# message=message[0:len(message):2]
# print(message)
r=""
le=len(message)
print(le)
while(le>0):
  r=r+message[le-1]
  le=le-1


print(r)