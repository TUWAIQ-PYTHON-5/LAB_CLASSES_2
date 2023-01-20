from bus import Bus
from truck import Truck


trace1=Truck('VOLVO','BIG Trace','GRAY','4','111SW',2.2)

print(f'Payload Weight {trace1.get_weight()} Tons')
trace1.drive()
trace1.carry_cargo()
print(trace1.print_vehicle_info())

print('*'*20)

bus1=Bus('GMC','GM BUS','YELLOW','50','123AB','3')

print(f'Name of Bus : {bus1.get_name()}')
bus1.drive()
bus1.drift()
print(bus1.print_vehicle_info())
