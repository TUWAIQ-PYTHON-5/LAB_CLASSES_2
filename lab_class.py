
class Vehicle:
    def __init__(self,  brand: str, name: str, color: str,capacity:int,plate_number:int):
        self.__brand = brand
        self.__name = name
        self.__color =color
        self.__capacity=capacity
        self.__plate_number=plate_number
    def drive(self):
          return f"the vehicle {self.__name} is driving!"
    
    def drift(self):
         return f"the vehicle {self.__name} is drifting !!"
    
    def carry_cargo(self):
         return f"the vehicle {self.__name} is carrying cargo !!"
    
    def  set_brand(self, brand):
         self.__brand = brand
    def get_brand(self):
        return self.__brand
    
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_color(self,color):
        self.__color=color
    def get_color(self,color):
        return self.__color
    
    def set_capacity(self,capacity):
        self.__capacity=capacity
    def get_capacity(self,capacity):
        return self.__capacity
    
    def set_plate_number(self,plate_number):
        self.__plate_number=plate_number
    def get_plate_number(self,plate_number):
        return self.__plate_number
car1=Vehicle("Toyota"," Van","red",6,403)
class  Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: float, plate_number: int):
        super().__init__(brand, name, color, capacity, plate_number)
    def drive(self):
          return f"the bus {self.get_name()} is driving!"
    
    def drift(self):
         return f"the bus {self.get_name()} is drifting !!"
    
    def carry_cargo(self):
         return f"the bus {self.get_name()} is carrying cargo !!"

bus1=Bus("Toyota"," Mini bus","white ",10,457)
class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: float, plate_number: int):
        super().__init__(brand, name, color, capacity, plate_number)
    def drive(self):
          return f"the truck {self.get_name()} is driving!"
    
    def drift(self):
         return f"the truck {self.get_name()} is drifting !!"
    
    def carry_cargo(self):
         return f"the truck {self.get_name()} is carrying cargo !!"

truck1=Truck("TATA","Big truck","black",3,766)
print(car1.get_brand,car1.get_name,car1.get_color,car1.get_capacity,car1.get_plate_number)
print(car1.drive())
print(car1.drift())
print(car1.carry_cargo())


print(bus1.get_brand,bus1.get_name,bus1.get_color,bus1.get_capacity,bus1.get_plate_number)
print(bus1.drive())
print(bus1.drift())
print(bus1.carry_cargo())


print(truck1.get_brand,truck1.get_name,truck1.get_color,truck1.get_capacity,truck1.get_plate_number)
print(truck1.drive())
print(truck1.drift())
print(truck1.carry_cargo())
    

    

