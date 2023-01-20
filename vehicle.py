class Vehicle:

    year:int=2023

    def __init__(self,brand:str,name:str,color:str,capacity:str,plate_number:str):  
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    
    def drive(self):
            print(f"The Vehicle : {self.get_name()} is driving")

    def drift(self):
        print(f"The Vehicle : {self.get_name()} is drifting !!")

    def carry_cargo(self):
        print(f"The Vehicle : {self.get_name()} is carrying cargo!!")

    def set_brand(self,brand:str):
        self.__brand = brand
        
    def get_brand(self):
        return self.__brand
        
    def set_name(self,name:str):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_color(self,color:str):
        self.__color = color
        
    def get_color(self):
        return self.__color

    def set_capacity(self,capacity:str):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def set_plate_number(self,plate_number:str):
        self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number
    
    def print_vehicle_info(self):
        return f"The Brand is : {self.get_brand()} and The Name is : {self.get_name()} also Color : {self.get_color()}\nThe Capacity are : {self.get_capacity()} The Number of plate : {self.get_plate_number()}  Year : {Vehicle.year}"

