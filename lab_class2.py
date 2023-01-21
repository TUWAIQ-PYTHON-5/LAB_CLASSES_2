from typing import Self


class Vehicle:
    kind="the_cars"
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int,driver:str,car_drift:str,cargo:str):
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number
        self.__driver=driver
        self.__car_drift=car_drift
        self.__cargo=cargo

    def set_brand(self,brand):
        self.__brand=brand
    def get_brand(self):
        return self.__brand
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
    def set_capacity(self,capacity):
        self.__capacity=capacity
    def get_capacity(self):
        return self.__capacity
    def set_plate_number(self,plate_number):
        self.__plate_number=plate_number
    def get_plate_number(self):
        return self.__plate_number 
    def set_car_drift(self,car_drift):
        self.__car_drift=car_drift
    def get_car_drift(self):
        return self.__car_drift  

    def drive(self):
     return f"the vehicle_name is driving!{self.__driver}"
    def drift(self):
         return f"{self.get_car_drift()} is drifting " 
    def arry_cargo(self):
     return f" {self.__cargo} is carrying cargo"


cars=Vehicle("Mercedes","G-class","black",7689644,9999,"sultan","mostang","the train")
print("information the vehical ",cars.drift())


class Bus(Vehicle):
     def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int,driver:str,car_drift:str,bus:str):
        self.__bus=bus
        super().__init__(brand,name,color,capacity,plate_number,driver,car_drift)
   

     def set_bus(self,bus):
        self.__bus=bus
     def get_bus(self):
       return self.__bus

     def drift(self):
         return f"{self.__bus} is not drifting "

cars1=Vehicle("nassan","G-class","black",7689644,9999,"sultan","bus","mostang")
print("information the vehical ",cars1.get_brand())




class Truck(Vehicle):
         def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int,driver:str,car_drift:str,bus:str,truck:str):
            self.__truck=truck
            super().__init__(brand,name,color,capacity,plate_number,driver,car_drift,bus)

         def set_truck(self,truck):
            self.__=truck
         def get_truck(self):
          return self.__truck
        

cars2=Vehicle("Mercedes","G-class","black",7689644,9999,"sultan","mostang","truck")
print("information the vehical ",cars1.get_name())
