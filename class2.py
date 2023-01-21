class Vehicle:

    def __init__(self, brand : str, name : str, color : str,  capacity : int, plate_number : int):
       self.__brand = brand
       self.__name = name
       self.__color = color
       self.__capacity = capacity
       self.__plate_number = plate_number

    def drive(self):
     print(f"the vehicle : {self.get_name()} is driving!")

    def drift(self):
     print(f"the vehicle : {self.get_name()} is drifting !!") 
    
    def carry_cargo(self):
     print(f"the vehicle : {self.get_name()} is carrying cargo !!")

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
        self.__capacity= capacity
    def get_capacity(self):
        return self.__capacity

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    def get_plate_number(self):
        return self.__plate_number


class Bus(Vehicle):
    def __init__(self, brand: str, name : str, color : int, capacity: str, plate_number : str, passengers):
        super().__init__(brand, name, color, capacity, plate_number)

        self._passengers = passengers

    def set_passengers(self,passengers):
        self.passengers = passengers

    def get_passengers(self):
        return self.get_passengers
    


class Truck(Vehicle):
    def __init__(self, brand: str, name : str, color : int, capacity: str, plate_number : int, Payload):
        super().__init__(brand, name, color, capacity, plate_number)
        self.payload = Payload

    def set_Payload(self,Payload):
        self.Payload = Payload
          
    def get_payload(self):
        return self.get_payload
    

bus = Bus("vOLVO", "1CB", "white", "88 kg", "DK678",90)
truck = Truck("scania", "raven", "black", "900kg", "sos765", "4,000 ibs")

print("Bus brand:", bus.get_brand())
print("Bus name:", bus.get_name())
print("Bus color:", bus.get_color())
print("Bus capacity:", bus.get_capacity())
print("Bus plate_number:", bus.get_plate_number())
print("Bus passengers:", bus.get_passengers())

print("Truck BRAND:", truck.get_brand())
print("Truck NAME:", truck.get_name())
print("Truck color:", truck.get_color())
print("Truck capacity:", truck.get_capacity())
print("Truck plate_number:", truck.get_plate_number())
print("Truck Payload:", truck.get_payload())