'''
Simple Start:
    Class setup:
    - Car
        - name/length/speed control
        - speed-up/slow-down
    - Road
        - length
        - location of car(s); starting with one
  '''

class Car:
    '''Standard car characteristics'''
    def __init__(self):
        self.car_length = 5     #  5 is the standard car length in meters.
        self.max_speed = 33     # 33 meters per second equivalent to 120 kilometers/sec.
        self.braking = 2        #  2 meters per second reduction randomly applied.
        self.velocity = 0       #  0 starting velocity
        self.location = 0       #  0 starting location

class Road:
    '''Highway characteristics and car locations [cashier example]'''
    def __init__(self, number_of_cars):
        self.number_of_cars = number_of_cars
        self.car = [Car() for _ in range(number_of_cars)]
        self.highway = 1000     # 1 kilometer is the standard segment for model.

    def accelerate(self):
        for car in self.car:
            vehicle = 1
            for t in range(30):    # set to 5 for testing
                if t == 0:
                    car.velocity = 0
                elif self.decelerate() == True and (car.velocity > 0):
                    car.velocity -= 2        #reduced by 2 meters per second
                    car.location += car.velocity
                else:
                    if car.velocity <= (car.max_speed - 3):
                        car.velocity += 2    #increased by 2 meters per second
                car.location += car.velocity
                if car.location > self.highway:
                    car.location = 0
                plt.scatter(car.location, car.velocity)
                plt.show

#                print("time: {}, velocity: {}, location: {} meters".format(t, car.velocity, car.location))
            vehicle += 1

    def decelerate(self):
        if random.random() < 0.1:
            return True
        else:
            return False
