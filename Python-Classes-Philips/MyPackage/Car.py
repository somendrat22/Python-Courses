class Car:
    wheels = 4
    totalEngines = 1
    steringWheels = 1

    def __init__(self, carBrand, carColor):
        self.carBrand = carBrand
        self.carColor = carColor


    def __str__(self):
        return "Car Details : {0} , {1}".format(self.carBrand, self.carColor)

    def playRadio(self):
        print("Hey in your car {0} radio started".format(self.carBrand))

    def calculateSpeed(self, dist, time):
        speed = dist/time
        print("Hey your car {0} is running at speed of {1} km/hr".format(self.carBrand, speed))