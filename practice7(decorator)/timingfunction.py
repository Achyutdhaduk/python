import time

def timer(func):
    def wrapper(*args,**kwargs):
       start = time.time()
       result =  func(*args,**kwargs)
       end = time.time() 
       print(f"{func.__name__} run in {end-start} time")
       return result
    return wrapper

  

@timer
def example_fun(n):
    time.sleep(n)   
example_fun(2)    
    
    