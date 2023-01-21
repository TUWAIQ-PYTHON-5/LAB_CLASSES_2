from Vehicle.Vehicles import Vehicle  


class Bus(Vehicle):

    def __init__(self, brand , name, color, capacity , plate_number ):
        super().__init__(brand, name, color, capacity, plate_number)

    def drift(self):
        return f"The Bus ({self.get_name()}) is not drifting! "
    
    def drive(self):
        return f"The Bus ({self.get_name()}) is driving!"

    def carry_cargo(self):
        return f"The Bus ({self.get_name()}) is to transport people !!"

