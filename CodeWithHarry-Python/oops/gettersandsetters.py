class Myclass:
  def __init__(self,value):
    self._value=value

  def show(self):
    print(f"the value is {self._value}")

  @property
  def value(self):
    return self._value
  @value.setter
  def set_val(self,newval):
    self._value=newval


obj=Myclass(10)
print(obj._value)
obj.set_val(20)
obj.show()