class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):


    def drive(self):
        print("Car is driving")



my_car = Car()
my_car.start()  # Output: Vehicle is starting
my_car.drive()  # Output: Car is driving
