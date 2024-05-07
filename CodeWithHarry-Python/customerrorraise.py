a=int(input("enter any value between 5 and 9"))
if(a<5 or a>9):
  raise ValueError("Value should between 5 and 9")