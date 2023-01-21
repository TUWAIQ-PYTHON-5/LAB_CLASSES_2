

class Vehicle:
    def __init__(self, brand : str, name : str, color : str , capacity : int, plate_number : int ) :
        self.__brand = brand 
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

# encabsulate the >>
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


#Methods
    def drift(self):
        return f"The truck {self.get_name()} is not drifting! "

    def drive(self):
        return f"The truck {self.get_name()} is not driving! "
            
    def carry_cargo(self):
        return f"The truck {self.get_name()} is carrying cargo !!"



# sub classes for bus and truck
class Bus (Vehicle) :
   
    def __init__(self, brand : str, name : str, color : str , capacity : int, plate_number : int):
        super().__init__(brand, name, color,capacity, plate_number )
        
        # methods bus
    def drift(self):
        return f"The truck {self.get_name()} is not drifting! "

    def drive(self):
        return f"The truck {self.get_name()} is not driving! "
            
    def carry_cargo(self):
        return f"The truck {self.get_name()} is carrying cargo !!"



class Truck (Vehicle):

    def __init__(self, brand : str, name : str, color : str , capacity : int, plate_number : int):
        super().__init__(brand, name, color,capacity, plate_number )

    # methods truck
    def drift(self):
        return f"The truck {self.get_name()} is not drifting! "

    def drive(self):
        return f"The truck {self.get_name()} is not driving! "
            
    def carry_cargo(self):
        return f"The truck {self.get_name()} is carrying cargo !!"



# The object from Vehicle class
Vehical_ = Vehicle ("BMW" , "X4M" , "Alpine White" , 3 , 5745 )
print("our Vehicle is :", Vehical_.get_brand(),","," The name is : ",Vehical_.get_name(), ","," The color is ",Vehical_.get_color(),",",
"The capacity and the palte number are : ",Vehical_.get_capacity(),",", Vehical_.get_plate_number() )
print(Vehical_.drive())
print(Vehical_.drift())
print(Vehical_.carry_cargo())
print("\n")


# The object from Bus sub class
Bus1 = Bus("Mercedes", "BRT", "Yellow", 8, 1999)
print("our Bus is :", Bus1.get_brand(),","," The name is : ",Bus1.get_name(),",", " The color is ",Bus1.get_color(),",",
"The capacity and the palte number are : ",Bus1.get_capacity(), ",", Bus1.get_plate_number() )
print(Bus1.drive())
print(Bus1.drift())
print(Bus1.carry_cargo())
print("\n")


## The object from Truck sub class
Truck1 = Truck("Mercedes", "Actros", "ًWhite", 10, 3478)
print("our truck is :", Truck1.get_brand(),",", "The name is : ",Truck1.get_name(), ","," The color is ",Truck1.get_color(),",",
"The capacity and the palte number are : ",Truck1.get_capacity(),",",Truck1.get_plate_number() )
print(Truck1.drive())
print(Truck1.drift())
print(Truck1.carry_cargo())