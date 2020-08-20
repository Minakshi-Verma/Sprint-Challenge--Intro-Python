# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle class is on the top of hierarchy 
class Vehicle:
    pass

# Vehicle is the base class  for GroundVehicle
class GroundVehicle(Vehicle):
    pass

# GroundVehicle is the base class for Car
class Car(GroundVehicle):
    pass

# GroundVehicle is the base class for Motorcycle
class Motorcycle(GroundVehicle):
    pass

# Vehicle is the base class for FlightVehicle
class FlightVehicle(Vehicle):
    pass

# FlightVehicle is the base class for Starship
class Starship(FlightVehicle):
    pass

# FlightVehicle is the base class for SAirplane
class Airplane(FlightVehicle):
    pass     

