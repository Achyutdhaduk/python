def f1(n):
    def f2(x):
        return x ** n
    return f2


f = f1(3)
z = f1(3)

print(f(2)) 
print(f(3))