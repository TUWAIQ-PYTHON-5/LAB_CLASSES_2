from ClassCAR_2 import Vehicle

class Truck(Vehicle):

    def __init__(self, brand , name, color, capacity , plate_number ):
        super().__init__(brand, name, color, capacity, plate_number)
      

    def drift(self):
        return f"The truck {self.get_name()} is not drifting! "

    def drive(self):
        return f"The truck {self.get_name()} is not driving! "
            
    def carry_cargo(self):
        return f"The truck {self.get_name()} is carrying cargo !!"