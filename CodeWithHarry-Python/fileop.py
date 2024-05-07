f=open("marks.txt","r")
i=0
while True:
 i=i+1
 line=f.readline()
 if not line:
  break
 m1=line.split(",")[0]
 m2=line.split(",")[1]
 m3=line.split(",")[2]
 print(f"Marks of student {i} in Maths is:{m1}")
 print(f"Marks of student {i} in eng is:{m2}")
 print(f"Marks of student {i} in GK is:{m3}")



fa=open("marks.txt","a")
content="a\nb\nc\n"
fa.writelines(content)