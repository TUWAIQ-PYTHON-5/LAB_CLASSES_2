
class Vehicle:

    def __init__(self, brand :str ,name :str ,color :str ,capacity: int ,plate_number :int):
        
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number


    
    def drive (self):
          return f"the {self.__name} is driving!"
    
    def drift(self):
        return f"the {self.__name} with plate number {self.__plate_number} is drifting !!"
   
    def comparing (self):
        return f"the {self.__brand} {self.__name} is way better in capasity than ford Taurus,Because it can fit {self.__capacity} passengers!!"

    def carry_cargo(self):
        return f"the {self.__brand} {self.__name} is carrying cargo !!"

    def set_brand(self, brand):
        self.__brand = brand
    
    def get_brand(self):
        return self.__brand
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
   
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

    def set_capacity(self, capacity):
        self.__capacity = capacity
    
    def get_capacity(self):
        return self.__capacity

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    
    def get_plate_number(self):
        return self.__plate_number

class Bus(Vehicle):

        def __init__(self, brand :str ,name :str ,color :str ,capacity: int ,plate_number :int, size :int):
         super().__init__(brand,name,color,capacity,plate_number)
         self.size = size
        
         def drive (self):
          return f"the {self.__name} with {self.size} is driving!"
      

class Truck(Vehicle):
    def __init__(self, brand :str ,name :str ,color :str ,capacity: int ,plate_number :int, cargo_capacity:int):
         super().__init__(brand,name,color,capacity,plate_number)
         self.cargo_capacity = cargo_capacity

vehicle_opject1 = Vehicle ("Toyota" , "Avalon" , "black" , 6 , 1243)
vehicle_opject2 = Vehicle ("Ford" , "Taurus" , "white" , 4 , 7896)
Bus1 = Bus("Mercedes","Intouro","white", 50, 2341 ,"12 meter")
Truck1 = Truck("Tata Motors","PRIMA","Red",2 ,1322, 5800)

    
print(vehicle_opject1.drive())
print(vehicle_opject2.drift())
print(vehicle_opject1.comparing())
vehicle_opject1.set_color("Silver")
vehicle_opject2.set_brand("BMW")
print("the best vehicle color for me is : " , vehicle_opject1.get_color())
print("the best vehicle brand for me is : " , vehicle_opject2.get_brand())
print(Bus1.drive())
print(Bus1.comparing())
print(Truck1.carry_cargo())
print(Truck1.comparing())









