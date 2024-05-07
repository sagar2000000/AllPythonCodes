class Person:

  def disp(self):
    print("I am a person")



class genz(Person):

  def dispg(self):
    print("i am genz kid")
    super().disp()




a=genz()
a.dispg()
