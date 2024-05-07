class Math:
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2
    
  def addtwonum(self):
    print(self.num1+self.num2)

  @staticmethod
  def adder(a,b):
    return a+b 



obj=Math(2,3)
obj.addtwonum()
print(obj.adder(2,4)) 