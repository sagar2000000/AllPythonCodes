def greet(fx):
  def mfx(*args):
    print("thanks for using me")
    fx(*args)
    
  return mfx


def adder(a,b):
  print(a+b)

greet(adder)(1,2)  