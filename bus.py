from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self,brand:str,name:str,color:str,capacity:str,plate_number:str,doors:str):
        super().__init__(brand,name,color,capacity,plate_number)
        
        self.__doors = doors
        
    def set_doors(self,doors:str):
        self.__doors = doors

    def get_doors(self):
        return self.__doors
    
    def drive(self):
        print(f"The Bus : {self.get_name()} is driving")

    def drift(self):
        print(f"The Bus : {self.get_name()} is drifting !!")
    
    def print_vehicle_info(self):
        return f"The Brand is : {self.get_brand()} and The Name is : {self.get_name()} also Color : {self.get_color()}\nNumber of doors : {self.get_doors()} Capacity are : {self.get_capacity()} The Number of plate : {self.get_plate_number()}  Year : {Vehicle.year}"
