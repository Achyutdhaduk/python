mark = 76

if mark >= 101:
    print("invalid input")
    exit()

if mark >=90:
    grade = 'A'
elif mark >=80:
    grade = 'B'
elif mark >=70:
    grade = 'c'        
elif mark >=60:
    grade = 'D'        
else :
    grade = 'E'        
    
    
print("Grade :",grade)