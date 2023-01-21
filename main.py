from Vehicle import Trucks , Buses , Vehicles


def Display(vehicle):

    print("----------------------------------") 
    print(f"The Vehicle Brand : {vehicle.get_brand()} , Name : {vehicle.get_name()} , Color : {vehicle.get_color()} , Capacity : {vehicle.get_capacity()} , No. : {vehicle.get_plate_numbere()} ")  
    print(vehicle.drift())
    print(vehicle.drive())
    print(vehicle.carry_cargo())
'''
_Car 
_Truck 
_Bus 
'''
Display(Vehicles.Vehicle("Nissan" , "Pickup" , "White" , 5 , 82122))
Display(Trucks.Truck("Volvo" , "FH16" , "Black" , 3 , 299932))
Display(Buses.Bus("Hyundai " , "County " , "Brown" , 15 , 300400))

    







