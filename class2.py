class Vehicle:

    def __init__(self, brand:str , name:str ,color:str ,capacity:int ,plate_number:int):

        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drift(self):
        return f"The truck {self.get_name()} is not drifting! "

    def drive(self):
        return f"The truck {self.get_name()} is not driving! "

    def carry_cargo(self):
        return f"The truck {self.get_name()} is carrying cargo !!"


        def set_name(self, name):
            self.__name = name

        def get_name(self):
            return self.__name

        def set_brand(self, brand):
            self.__brand = brand

        def get_brand(self):
            return self.__brand

        def set_color(self, color):
            self.__color = color

        def get_color(self):
            return self.__color

        def set_capacity(self, capacity):
            self.__capacity = capacity

        def get_capacity(self):
            return self.__capacity

        def set_plate_number(self, plate_number):
            self.__Plate_number = plate_number

        def get_plate_number(self):
            return self.__plate_number



class Bus(Vehicle):

        def _init_(self, brand: str, name: str, color: str, capacity: int, plate_number: int):
            super()._init_(brand, name, color, capacity, plate_number)


        def drift(self):
            return f"The truck {self.get_name()} is not drifting! "

        def drive(self):
            return f"The truck {self.get_name()} is not driving! "

        def carry_cargo(self):
            return f"The truck {self.get_name()} is carrying cargo !!"

class Truck(Vehicle):

        def _init_(self, brand: str, name: str, color: str, capacity: int, plate_number: int):
            super()._init_(brand, name, color, capacity, plate_number)


        def drift(self):
            return f"The truck {self.get_name()} is not drifting! "

        def drive(self):
            return f"The truck {self.get_name()} is not driving! "

        def carry_cargo(self):
            return f"The truck {self.get_name()} is carrying cargo !!"

Vehical1 = Vehicle("Lexus", "GX", "black", 6, 8890)
print("Vehicle is :", Vehical1.get_brand(), ",", " name is : ", Vehical1.get_name(), ",", " color is ",
          Vehical1.get_color(), ",",
          "capacity and the palte number  : ", Vehical1.get_capacity(), Vehical1.get_plate_number())
print(Vehical1.drive())
print(Vehical1.drift())
print(Vehical1.carry_cargo())
print("\n")


Bus1 = Bus("Mercedes", "g-class", "White", 9, 2000)

print("Bus is :", Bus1.get_brand(), ",", "name is : ", Bus1.get_name(), ",", "color is ",
          Bus1.get_color(), ",",
          "capacity and the palte number  : ", Bus1.get_capacity(), "\n", Bus1.get_plate_number())
print(Bus1.drive())
print(Bus1.drift())
print(Bus1.carry_cargo())
print("\n")


Truck1 = Truck("Mazda", "Mazda6 ", "ًWhite", 7, 10705)

print("truck is :", Truck1.get_brand(), ",", "name is : ", Truck1.get_name(), ",", " color is ",
          Truck1.get_color(), ",",
          "capacity and the palte number  : ", Truck1.get_capacity(), ",", Truck1.get_plate_number())
print(Truck1.drive())
print(Truck1.drift())
print(Truck1.carry_cargo())


