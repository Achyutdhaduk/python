x= 99

def fun():
    global x
    print(x)
    x=10
    print("fun x:",x)
    x =12
    
print("Global X:",x) 
fun()    
print("After fun() X:",x)  

""" 
-> Give Comment global x check output"""