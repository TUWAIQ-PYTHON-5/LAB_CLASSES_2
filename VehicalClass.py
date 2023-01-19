class Vehical:

    def __init__(self , brand :str , name:str , color :str , capacity : int , plat_number : int) -> None:
        self.__brand = brand
        self.__color = color
        self.__capacity = capacity
        self.__plat_number = plat_number
        self.__name = name


    def set_name(self , name :str):
        self.__name = name

    def get_name(self ):
        return self.__name      


    def set_brand(self , brand):
        self.__brand = brand

    def get_brand(self ):
        return self.__brand   


    def set_color(self , color):
        self.__color = color

    def get_color(self ):
        return self.__color    

    def set_capacity(self , capacity):
        self.__capacity = capacity

    def get_capacity(self ):
        return self.__capacity    

    def set_plat_number(self , plat_number):
        self.__plat_number = plat_number

    def get_brand(self ):
        return self.__plat_number  


    def drive(self)-> str:
        return f"the {self.get_name()}is driving!"

    def drift(self):
        return f"the {self.get_name()} is drifting "

    def carry_cargo(self):        
        return f"the {self.get_name()} is carry_cargo"

class bus(Vehical):
    
    def __init__(self, brand : str, name : str, color : str, capacity :int, plat_number : int ):
        super().__init__(name, brand, color  , capacity ,plat_number )

    def drive(self)-> str:
            return f"the {self.get_name()}is driving!"

    def drift(self):
        return f"the {self.get_name()} is not drifting it is for transportation "

    def carry_cargo(self ):        
        return f"the {self.get_name()} is carry_cargo "

class truck(Vehical):
    
    def __init__(self, brand : str, name : str, color : str, capacity :int, plat_number : int ):
        super().__init__(name, brand, color  , capacity ,plat_number )

    def drive(self)-> str:
            return f"the {self.get_name()} is driving! "

    def drift(self):
        return f"the {self.get_name()} is not drifting "

    def carry_cargo(self ):        
        return f"the {self.get_name()} is carry_cargo "



vehicalOne = Vehical("TOYOTA" , "CAR123" , "RED" , 5 , 123400 )
print("First Vehicall is :" , vehicalOne.get_name() , "AND COLOR IS " , vehicalOne.get_color() )
print(vehicalOne.drive())
print(vehicalOne.drift())
print(vehicalOne.carry_cargo())
print("____"* 10)

truckOne = truck ("TRACKname - A" , "TRACK -A " , "BLACK" , 2 , 15477714200)
print("First truck is :" , truckOne.get_name() , "AND COLOR IS " , truckOne.get_capacity() )
print(truckOne.drive())
print(truckOne.drift())
print(truckOne.carry_cargo())
print("____"* 10)

busOne = bus("BUSname " , "bus -A " , "yellow" , 30 , 14200)
print("First bus is :" , busOne.get_name() , "AND COLOR IS " , busOne.get_capacity() )
print(busOne.drive())
print(busOne.drift())
print(busOne.carry_cargo())
print("____"* 10)



