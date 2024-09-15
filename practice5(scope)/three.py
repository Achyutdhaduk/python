x=99
def f1():
    def f2():
        print(x)
    f2()
 
 
def f3():
    x=12
    def f4():
        print(x)
    f4()    
   
   
        
f1()

f3()

                