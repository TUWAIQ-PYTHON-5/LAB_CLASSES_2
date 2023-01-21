class Vehicle :
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : int) :
        self.__brand = brand
        self.__name = name 
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def set_brand(self, brand) :
        self.__brand = brand
    def get_brand(self) :
        return self.__brand

    def set_name(self, name) :
        self.__name = name
    def get_name(self) :
        return self.__name

    def set_color(self, color) :
        self.__color = color
    def get_color(self) :
        return self.__color

    def set_capacity(self, capacity) :
        self.__capacity = capacity
    def get_capacity(self) :
        return self.__capacity

    def set_plate_number(self, plate_number) :
        self.__plate_number= plate_number
    def get_plate_number(self) :
        return self.__plate_number

    
    
    def drive(self) :
        print(f"the {self.get_name()} is is driving!")

    def drift(self) :
        print(f"the {self.get_name()} is is drifting !!")

    def carry_cargo(self) :
        print(f"the {self.get_name()} is carrying cargo !!")




class Bus(Vehicle) :
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : int) :
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self) :
        print(f"the {self.get_name()} is driving! (Bus driving)")

    def drift(self) :
        print(f"the {self.get_name()} is drifting !! (Bus drifting)")

    def carry_cargo(self) :
        print(f"the {self.get_name()} is carrying cargo !! (Bus carrying cargo)")


class Truck(Vehicle) :
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : int) :
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self) :
        print(f"the {self.get_name()} is driving! (Truck driving)")
    
    def drift(self) :
        print(f"the {self.get_name()} is drifting !! (Truck drifting)")

    def carry_cargo(self) :
        print(f"the {self.get_name()} is carrying cargo !! (Truck carry cargo)")

camry = Vehicle(2020, "camery", "white", 5, 1122 )

bus1 = Bus(2021, "tayotaBus", "blue", 20, 1234)

truck1 = Truck(2022, "truckXX", "gray", 3, 4444)

camry.drive()
camry.drift()
camry.carry_cargo()

print("*"*10)

bus1.drive()
bus1.drift()
bus1.carry_cargo()

print("*"*10)

truck1.drive()
truck1.drift()
truck1.carry_cargo()
    
