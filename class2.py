class Vehicle:
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : int):
        self.__brand = brand 
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

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
        self.__color = capacity
    
    def get_capacity(self):
        return self.__capacity


    def set_plate_number(self, plate_number):
        self.__color = plate_number
    
    def get_capacity(self):
        return self.__plate_number


    def drive(self):
        return f"the{self.get_name()} is driving!"

    def drift(self):
        return f"the{self.get_name()} is drifting !!"
    
    def carry_cargo(self):
        return f"the{self.get_name()} is carrying cargo !!"

    
class Truck(Vehicle):
    
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : int):
        super().__init__(brand, name, color, capacity, plate_number)
    
    def drive(self):
        return f"the{self.get_name()} is driving!"

    def drift(self):
        return f"the {self.get_name()}is drifting!!"
    
    def carry_cargo(self):
        return f"{self.get_name()}is carrying cargo!!"



class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int):
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self):
        return f"the{self.get_name()} is driving!"

    def drift(self):
        return f"the {self.get_name()}is drifting!!"
    
    def carry_cargo(self):
        return f" {self.get_name()}is carrying cargo!!"

vehical_1 = Vehicle ("Mercedes-Benz" , "Truck" , "RED" , 2 , 5231744 )
print(vehical_1.drive())
print(vehical_1.drift())
print(vehical_1.carry_cargo())


bus_1 = Bus(" toyota " , " Hays " , " white " , 15 , 201445)
print(bus_1.drive())
print(bus_1.drift())
print(bus_1.carry_cargo())


truck = Truck(" truck_a " , " name_truck " , " white " , 5 , 85236997)
print(bus_1.drive())
print(bus_1.drift())
print(bus_1.carry_cargo())