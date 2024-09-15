""" 
-> property decorator no use readonly karva mate thai ama change no kari sako
"""

class car: 
    totalcar= 0
    def __init__(self,brand,model):
        self.__brand= brand
        self.__model= model
        # print(self.brand,self.model)
        # print(f"{self.brand} {self.model}")
        # print(self.__model)
        self.item = 111
        car.totalcar += 1
        
    def fullname(self):
        return f"{self.__brand} {self.__model}" 
    
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "petrol or diesel"
        
    @property
    def get_model(self):
         return self.__model


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
# my_car1.__model='ACHYUT'
# print(my_car1.get_model)
# print(my_car1.__model)

# my_car2 = car('toyota','for..')
# print(f.brand)
# print(f.model)
# print(f.item)
# result =my_car.fullname()
# print(result)

my_car=Electriccar('tata','safari','80Kwh')

# print(isinstance(my_car,car))
# print(isinstance(my_car,Electriccar))

# print(isinstance(my_car1,car))
# print(isinstance(my_car1,Electriccar))


# print(my_car.__brand)
# print(my_car.fullname())
# print(my_car.get_brand())
# print(my_car1.__brand) error ave private direct use no kari saki

# print(my_car.fuel_type())
# print(my_car1.fuel_type())

# print(my_car.totalcar)
# print(car.totalcar)


class Battery:
    def bett(self):
        return "This is class Battery"

class Engine:
    def eng(self):
        return "This is class Engine"

class ElectricTwo(Battery,Engine,car):
    pass


result = ElectricTwo('tesla', 'model s')
print(result.bett())
print(result.eng())
        