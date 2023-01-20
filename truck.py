from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self,brand:str,name:str,color:str,capacity:str,plate_number:str,weight:float):
        super().__init__(brand,name,color,capacity,plate_number)

        self.__weight = weight

    def set_weight(self,weight:float):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def drive(self):
        print(f"The Truck : {self.get_name()} is driving")

    def carry_cargo(self):
        print(f"The Truck : {self.get_name()} is carrying cargo!!")

    def print_vehicle_info(self):
        return f"The Brand is : {self.get_brand()} and The Name is : {self.get_name()} also Color : {self.get_color()}\nPayload weight : {self.get_weight()} Tons The Capacity are : {self.get_capacity()} The Number of plate : {self.get_plate_number()}  Year : {Vehicle.year}"

