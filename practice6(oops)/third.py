class car: 
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
        # print(self.brand,self.model)
        # print(f"{self.brand} {self.model}")
        
        self.item = 111
        
    def fullname(self):
        return f"{self.brand} {self.model}" 


class Electriccar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        print(self.battery_size)
        print(brand)
        print(model)
        
        
        
        
        
# my_car = car('toyota','innova')
# print(f.brand)
# print(f.model)
# print(f.item)
# result =my_car.fullname()
# print(result)

my_car=Electriccar('tata','safari','80Kwh')
print(my_car.model)
print(my_car.fullname())
