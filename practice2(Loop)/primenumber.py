number =10


for i in range(3,number+1):
    b = False
    for j in range(2,i):
        if (i%j==0):
            b = True
            break
        else:
            continue
           
    if(b != True):
        print(i)
        
            