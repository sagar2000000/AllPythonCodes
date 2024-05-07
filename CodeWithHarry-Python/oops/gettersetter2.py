class Person:
  def set(self,name,age):
    self.name=name
    self.age=age

  def get(self):
    print(f"the name is {self.name} and age is {self.age}")  




obj=Person()
obj.set("sagar",20)    
obj.get()