class Person:
  def set(self,name,age):
    self.name=name
    self.age=age

  def get(self):
    print(f"the name is {self.name} and age is {self.age}")  

class Employee(Person):
  def identify(self):
    print("hello i am a employee")


obj=Employee()
obj.set("sagar",20)    
obj.get()
obj.identify()