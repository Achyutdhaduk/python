class car: 
    def __init__(self,brand,model):
        self.__brand= brand
        self.model= model
        # print(self.brand,self.model)
        # print(f"{self.brand} {self.model}")
        
        self.item = 111
        
    def fullname(self):
        return f"{self.__brand} {self.model}" 
    
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "petrol or diesel"
        
        


class Electriccar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
            # print(self.battery_size)
            # print(brand)
            # print(model)
    
    def fuel_type(self):
        
        return "electric"
        
        
        
        
        
my_car1 = car('toyota','innova')
# print(f.brand)
# print(f.model)
# print(f.item)
# result =my_car.fullname()
# print(result)

my_car=Electriccar('tata','safari','80Kwh')
# print(my_car.__brand)
# print(my_car.fullname())
# print(my_car.get_brand())
# print(my_car1.__brand) error ave private direct use no kari saki

print(my_car.fuel_type())
print(my_car1.fuel_type())
