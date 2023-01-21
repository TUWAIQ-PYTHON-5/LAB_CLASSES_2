class Vehicle:
    def __init__ (self,brand :str,name :str,color:str,capacity:int,plate_number:int):
          self.__brand = brand
          self.__name = name 
          self.__color = color
          self.__capacity = capacity
          self.__plate_number = plate_number

    def drive(self):
        return f"the {self.__name} is driving"

    def drift(self):
        return f"the {self.__name} is drifting !!"

    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!"


    def set_brand(self,new_brand):
            self.__brand= new_brand

    def get_brand(self):
            return self.__brand

    def set_name(self,new_name):
            self.__name = new_name

    def get_name(self):
            return self.__name  

    def set_color(self,new_color):
            self.__color=new_color

    def get_color(self):
            return self.__color

    def set_capacity(self,new_capacity):
            self.__capacity=new_capacity

    def get_capacity(self):
            return self.__capacity

    def set_plate_number(self,new_plate_number):
            self.__plate_number=new_plate_number

    def get_plate_number(self):
            return self.__plate_number

       

class Bus(Vehicle):
    def __init__ (self,brand :str,name :str,color:str,capacity:int,plate_number:int):
        super().__init__(brand,name,color,capacity,plate_number)

    def drive(self):
            return f"the {self.get_name()} is driving to school"




class Truck(Vehicle):
    def __init__ (self,brand :str,name :str,color:str,capacity:int,plate_number:int):
        super().__init__(brand,name,color,capacity,plate_number)

    
    def carry_cargo(self):
        return f"the {self.get_name()} is carrying furniture !"


Vehicle_1=Vehicle("LEXUS","RC-F","BLACK",3500,7777)
Vehicle_2=Bus("Bus-5","B-5","white",4000,2358)
Vehicle_3=Truck("Truck-8","T-8","yellow",6000,9522)

print(Vehicle_1.drift())
print(Vehicle_1.drive())
print(Vehicle_1.carry_cargo())


print(Vehicle_2.drive())

print(Vehicle_3.carry_cargo())