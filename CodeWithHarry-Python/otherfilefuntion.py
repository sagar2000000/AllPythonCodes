with open('sagar.txt','r') as f:
 print(type(f))
 f.seek(5)
#  data=f.read(5)
#  print(data)
 print(f.tell())

with open('sagar.txt','w') as f: 
 f.write("123456789")
 f.truncate(5)
 