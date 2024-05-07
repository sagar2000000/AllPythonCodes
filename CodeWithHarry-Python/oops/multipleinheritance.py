class Employee:
  def __init__(self,name):
    self.name=name
  def show(self):
    print(f"The name is {self.name}")
class Dancer:
  def __init__(self,dance):
    self.dance=dance
  
  def show(self):
    print(f"The dance name is{self.dance} ")

class DancerEmploye(Employee,Dancer):
    def __init__(self, name,dance):
      self.name=name
      self.dance=dance

      
de=DancerEmploye("sagar","breakdance")      
de.show()