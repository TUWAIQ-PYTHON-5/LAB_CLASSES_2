#to define a class
class Vehicle :
    #class Attribute / Property
    

    def __init__(self, brand  : str, name : int, color : str,capacity , plate_number):
        #initialize object / instance attributes
        self.brand = brand
        self.name = name #attribute is private / encapsulation
        self.color = color
        self.capacity = capacity
        self.plate_number= plate_number
    
    def set_brand(self, brand):
        self.brand = brand
    
    def get_brand(self):
        return self.__brand

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_color(self, color):
        self.color = color 
    
    def get_color(self):
        return self.color

    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def get_capacity(self):
        return self.capacity

    def set_plate_number(self, plate_number):
        self.plate_number = plate_number
    
    def get_plate_number(self):
        return self.plate_number
    

    def drive():
        return f"The {self.get_name()} is driving ."
    def drift():
        return f"The  {self.get_name()} is drifting ." 
    def carry_cargo():
        return f"The {self.get_name()} is carrying cargo ." 


class Bus(Vehicle):
    def __init__(self, brand: str, name: int, color: str, capacity, plate_number, driver_name ):
        super().__init__(brand, name, color, capacity, plate_number)
        self.driver_name = driver_name

    def drive():
        return f"The {self.get_name()} is driving ."
    def drift():
        return f"The  {self.get_name()} is drifting ." 
    def carry_cargo():
        return f"The {self.get_name()} is carrying cargo ." 


class Truck (Vehicle):
    def __init__(self, brand: str, name: int, color: str, capacity, plate_number,size ):
        super().__init__(brand, name, color, capacity, plate_number)
        self.size = size 

    def drive():
        return f"The {self.get_name()} is driving ."
    def drift():
        return f"The  {self.get_name()} is drifting ." 
    def carry_cargo():
        return f"The {self.get_name()} is carrying cargo ." 


vehile1 = Vehicle("TOYOTA" , "toyota" , "black" , 2 , 4546757 )
print("First Vehicall is :" , vehile1.get_name() , "from The brand " , vehile1.get_brand() )
print(vehile1.drive())
print(vehile1.drift())
print(vehile1.carry_cargo())
print("*"* 10)


Bus1 = Bus("BUSname " , " Mercedes" , "yellow" , 19 , 57676 , 150)
print("First bus is :" , Bus1.get_name() , "from the brand : " , Bus1.get_brand() )
print(Bus1.drive())
print(Bus1.drift())
print(Bus1.carry_cargo())
print("*"* 10)


truck1 = Truck("traucks" , "mani" , "Red" , 5, 989897)
print("First truck is :" , truck1.get_name() , "and color is" , truck1.get_color() )
print(truck1.drive())
print(truck1.drift())
print(truck1.carry_cargo())
print("*"* 10)
    