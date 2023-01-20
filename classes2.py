class Vehical:

    def __init__(self , brand :str , name:str , color :str , capacity : int , plate_number : int) -> None:
        self.__brand = brand
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
        self.__name = name
# __________driving method ________
    def drive(self)-> str:
        return f"the {self.get_name()}is driving!"
    def drift(self):
        return f"the {self.get_name()} is drifting "
    def carry_cargo(self):        
        return f"the {self.get_name()} is carry_cargo"
#_____________________________________
    def set_brand(self , brand):
        self.__brand = brand

    def get_brand(self ):
        return self.__brand   

#____________________
    def set_color(self , color):
        self.__color = color

    def get_color(self ):
        return self.__color    
#____________________
    def set_capacity(self , capacity):
        self.__capacity = capacity

    def get_capacity(self ):
        return self.__capacity    
#________________________
    def set_plate_number(self , plate_number):
        self.__plate_number = plate_number

    def get_plate_number(self ):
        return self.__plate_number  

#________________

    def set_name(self , name :str):
        self.__name = name

    def get_name(self ):
        return self.__name   

# sub classes _________________________

class bus(Vehical):
    def __init__(self, brand : str, name : str, color : str, capacity :int, plat_number : int ):
        super().__init__(name, brand, color  , capacity ,plat_number )
    def drive(self)-> str:
        return f"the {self.get_name()}is driving!"
    def drift(self):
        return f"the {self.get_name()} is drifting "
    def carry_cargo(self):        
        return f"the {self.get_name()} is carry_cargo"
##______________________________     

class truck(Vehical):
    def __init__(self, brand : str, name : str, color : str, capacity :int, plate_number : int ):
        super().__init__(name, brand, color  , capacity ,plate_number )
    def drive(self)-> str:
        return f"the {self.get_name()}is driving!"
    def drift(self):
        return f"the {self.get_name()} is drifting "
    def carry_cargo(self):        
        return f"the {self.get_name()} is carry_cargo"
#______________________________
vehica1 = Vehical("toyota" , "Rav4" , "Red" , 5 , 3324 )
print(" Vehical1 is :" , vehica1.get_brand() , vehica1.get_name() , "the capacity it : ", vehica1.get_capacity() ,"and its color is :  ", vehica1.get_color() )
print(vehica1.drive())
print(vehica1.drift())
print(vehica1.carry_cargo())
print("_______________________________________________")

#______________________________
truck1 = truck ("Volvo  " , " FM " , "BLACK" , 2 , 6657)
print(" truck 1 is :" , truck1.get_brand() , truck1.get_name() , "the capacity it :", truck1.get_capacity() ,"and its color is : ", truck1.get_color() )
print(truck1.drive())
print(truck1.drift())
print(truck1.carry_cargo())
print("_______________________________________________")

#______________________________
bus1 = bus("school bus " , "bus " , "yellow" , 20 , 14200)
print(" bus1  is :" , bus1.get_brand() , bus1.get_name() , "the capacity it : ", bus1.get_capacity() ,"and its color is : ", bus1.get_color() )
print(bus1.drive())
print(bus1.drift())
print(bus1.carry_cargo())
print("_______________________________________________")


##############################################
