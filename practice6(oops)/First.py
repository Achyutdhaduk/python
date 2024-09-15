class first: 
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
        print(self.brand,self.model)
        print(f"{self.brand} {self.model}")
        
        self.item = 111
        
        
f = first('toyota','innova')
print(f.brand)
print(f.model)
print(f.item)

        