class Vehicle:

    def __init__(self ,brand :str,name :str,color :str, capacity :int, plate_number :int):
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number

    def set_brand(self, brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
    def set_capacity(self, capacity):
        self.__capacity=capacity
    def get_capacity(self):
        return self.__capacity
    def set_plate_number(self,plate_number):
        self.__plate_number
    def get_plate_number(self):
        self.__plate_number

    def drive(self):
        print(f"the {self.name} is driving!")
    def drift(self):
        print(f"the {self.name} is drifting !!")
    def carry_cargo(self):
        print(f"the {self.name} is carrying cargo !!")

class Bus(Vehicle):

    def drive(self):
        print(f"the {self.get_name()} is driving!")

    def drift(self):
        print(f"the {self.get_name()} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.get_name()} is carrying cargo !!")
class Truck(Vehicle):
    def drive(self):
        print(f"the {self.get_name()} is driving!")

    def drift(self):
        print(f"the {self.get_name()} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.get_name()} is carrying cargo !!")


#vehicle_object=Vehicle("Rolls Royce","motor","black",7000,5984)
bus_object= Bus("Rolls Royce","motor","black",7000,5984)
#truk_object= Truck()
print(bus_object.drive())
