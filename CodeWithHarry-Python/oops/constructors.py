class Person:
  def __init__(self,n1,n2):
    self.num1=n1
    self.num2=n2

  def adder(self):
   print(f"the sum is {self.num1+self.num2}")
  


obj=Person(20,30)  
obj.adder()