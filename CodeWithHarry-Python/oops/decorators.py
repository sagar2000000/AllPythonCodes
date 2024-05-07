def greet(fx):
 def mfx(): 
   
   
   fx()
   print("thanks for using this function")
 return mfx

# @greet
def hello():
  print("hello world")


greet(hello)()