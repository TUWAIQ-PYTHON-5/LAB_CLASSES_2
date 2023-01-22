'''
# LAB_CLASSES_2

## define a Vehicle class . it has the following structure :

#### properties
- brand
- name
- color
- capacity
- plate_number


#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class


### for each of the properties do a setter & getter (encabsulate the data).

### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck


### Note
- override  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 
'''
class Vehicle: 
    def __init__(self, brand, name, color, capacity, plate_number): 
        self.__brand=brand 
        self.__name=name 
        self.__color=color 
        self.__capacity=capacity 
        self.__plate_number=plate_number 
    
    def set_brand(self, brand):
        self.__brand=brand 
        
    def get_brand(self): 
        return self.__brand 
  
    def set_name(self,name): 
        self.__name=name 
  
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
  
  
    def drive(self) : 
        print(f"{self.__name} is driving!") 

    def drift(self): 
        print( f"{self.__name} is drifting!!") 
  
    def carry_cargo(self): 
        print(f"{self.__name} is carrying cargo!!") 
    def print_all(self): 
        print(f"{self.get_brand()}, {self.get_name()}, {self.get_color()}, {self.get_capacity()}, {self.get_plate_number()}") 
 
class Bus(Vehicle): 
    def drift(self): 
        print(f"{self.get_name()} is not drifting") 
  
class Truck(Vehicle): 
    def drift(self): 
        print(f"{self.get_name()} ", " is not drifting") 
  
car_1=Vehicle("Chevrolet", "Silverado", "Black", 2, 299) 
car_1.print_all() 
car_1.drive() 
car_1.drift() 
car_1.carry_cargo()  

Bus_1=Bus("Toyota", "Hiace", "Grey" ,12 , 922) 
Bus_1.print_all() 
Bus_1.drive() 
Bus_1.drift() 
Bus_1.carry_cargo()