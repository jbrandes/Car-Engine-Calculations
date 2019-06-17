class Engine:
    
    def __init__(self, torque, rpm, horsepower, cylinders, displacement, bore, stroke, fuel_injector_size):
        
        self.torque = int(torque)
        self.rpm = int(rpm)
        self.cylinders = cylinders
        
        
print("Let's see how your car is running. Tell me about your car.")
torque = int(input("What is your torque? "))
rpm = int(input("What is your car's RPM? "))
cylinders = int(input("how many cylinders do you have? "))
Bore = int(input("how long is your engine bore measurement? "))
Stroke = int(input("What is the engine stroke measurement? "))
horsepower = ((rpm * torque) / 5252)
displacement = (cylinders * 0.7854 * (Bore**2) * Stroke)
fuel_injector_size = (horsepower / 16)

        
print("Your horsepower is: ", horsepower) 
print("Your engine displacement is: ", displacement, "CCs")
print("your fuel injector size is: ", fuel_injector_size, "lbs/hr")
    
if horsepower > 300:
    print("I don't know if that's steet legal")
else:
    print("You should look into a faster car.")
    
    
