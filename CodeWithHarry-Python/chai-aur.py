import time 
def timer(func):
  def wrapper(*args,**kwargs):
     starttime=time.time()
     result=func(*args,**kwargs)
     endtime=time.time()
     print(f"the time taken by {func.__name__} is {endtime-starttime}")
     return result
  return wrapper

@timer  
def example(n):
   time.sleep(n)



example(2)