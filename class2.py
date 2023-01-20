class Vehicle:


    def __init__(self, brand : str, name : str, color : str , capacity : int, plate_number : int ) -> None :
        
        self.__brand = brand 
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

# encabsulate the name
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
# encabsulate the brand
    def set_brand(self, brand):
        self.__brand = brand
    
    def get_brand(self):
        return self.__brand
# encabsulate the color
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

# encabsulate the capacity
    def set_capacity(self, capacity):
        self.__capacity = capacity
    
    def get_capacity(self):
        return self.__capacity

# encabsulate the plate_number

    def set_plate_number(self, plate_number):
        self.__Plate_number = plate_number
    
    def get_plate_number(self):
        return self.__plate_number

    def drive(self) -> str:
        return f"the {self.get_name()}is driving!"

    def drift(self):
        return f"the {self.get_name()} is drifting! "

    def carry_cargo(self):
        return f"the {self.get_name()} is carry_cargo!"



# sub classes for bus and truck

class Bus (Vehicle) :
   
    def __init__(self, brand : str, name : str, color : str , capacity : int, plate_number : int):
        super().__init__(brand, name, color,capacity, plate_number )
        
        # methods bus

    def drive(self) -> str:
        return f"the {self.get_name()}is driving!"

   
    def drift(self):
        return f"the {self.get_name()} is not drifting it is for transportation! "

    def carry_cargo(self):
        return f"the {self.get_name()} is carry_cargo! "




class Truck (Vehicle):

    def __init__(self, brand : str, name : str, color : str , capacity : int, plate_number : int):
        super().__init__(brand, name, color,capacity, plate_number )

    # methods truck
    
    def drive(self) -> str:
         return f"the {self.get_name()} is driving! "

    
    def drift(self):
        return f"the {self.get_name()} is not drifting! "

    def carry_cargo(self):
        return f"the {self.get_name()} is carry_cargo! "


# The object from Vehicle class

Vehical1 = Vehicle ("BMW" , "X4M" , "Alpine White" , 3 , 93334 )
print("our Vehicle is :", Vehical1.get_brand(),"2- The name is : ",Vehical1.get_name(), "3- The color is ",Vehical1.get_color(),
"The capacity and the palte number are : ",Vehical1.get_capacity(), "\n", Vehical1.get_plate_number() )

print(Vehical1.drive())
print(Vehical1.drift())
print(Vehical1.carry_cargo())
print("\n")

# The object from Bus sub class

Bus1 = Bus("Mercedes", "BRT", "Yellow", 8, 1999)
print("our Bus is :", Bus1.get_brand(),"2- The name is : ",Bus1.get_name(), "3- The color is ",Bus1.get_color(),
"The capacity and the palte number are : ",Bus1.get_capacity(), "\n", Bus1.get_plate_number() )

print(Bus1.drive())
print(Bus1.drift())
print(Bus1.carry_cargo())
print("\n")



## The object from Truck sub class

Truck1 = Truck("Mercedes", "Actros", "ًWhite", 10, 10506)
print("our truck is :", Truck1.get_brand(),"2- The name is : ",Truck1.get_name(), "3- The color is ",Truck1.get_color(),
"The capacity and the palte number are : ",Truck1.get_capacity(), "\n", Truck1.get_plate_number() )
print(Truck1.drive())
print(Truck1.drift())
print(Truck1.carry_cargo())
print("\n")

