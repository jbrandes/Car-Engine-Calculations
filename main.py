class Engine:
    
    def __init__(self, torque, rpm, horsepower, cylinders, displacement, bore, stroke, fuel_injector_size, tire_size, wheel_axle_ratio, gear_ratio, year, make, model):
        
        self.torque = int(torque)
        self.rpm = int(rpm)
        self.cylinders = cylinders
        
        
print("Let's see how your car is running. Tell me about your car.")
year = int(input("How year did you get your car? "))
make = input("What make is it? ")
model = input("What model? ")

if year < 2010:
    print("Your car is getting pretty old.")

torque = int(input("What is your torque? "))
rpm = int(input("What is your car's RPM? "))
cylinders = int(input("how many cylinders do you have? "))
Bore = int(input("how long is your engine bore measurement? "))
Stroke = int(input("What is the engine stroke measurement? "))
tire_size = int(input("What is your tire size? "))
gear_ratio = int(input("What is your gear ratio? "))
wheel_axle_ratio = int(input("What is your wheel axle ratio? "))
horsepower = ((rpm * torque) / 5252)
displacement = (cylinders * 0.7854 * (Bore**2) * Stroke)
fuel_injector_size = (horsepower / 16)
V = ((rpm * 3.14 * tire_size) / (gear_ratio * wheel_axle_ratio))
        
print("Your horsepower is: ", horsepower) 
print("Your engine displacement is: ", displacement, "CCs")
print("Your fuel injector size is: ", fuel_injector_size, "lbs/hr")
print("Your car's estimated velocity is: ", V, "mph")
    
if horsepower > 300:
    print("I don't know if that's steet legal")
else:
    print("You should look into a faster car.")
    

    
