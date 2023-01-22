class vehicle:
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int):
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number


    def drive(self,driver):
        self.driver=driver
        print (f"the vehicle_name is {driver}!")

    def drift(self,drifter):
        self.drifter=drifter
        print(f"the vehicle_name is {drifter}")

    def carry_cargo(self,cargo):
        self.cargo=cargo


class Bus(vehicle):

    pass


class Truck(vehicle):

    pass