class Employee:
  name="hii"
  company="Apple"
  def show(self):
    print(f"the name is{self.name} and company is {self.company}")

  def changeCompany(self,c):


    self.company=c  

e=Employee()
e.changeCompany("sagar")
e.show()