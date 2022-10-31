class Auto:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('Engine started')
        else:
            print('Engine already started')

    def stop_engine(self):
        self.engine = False
        print('Engine stopped')

    def accelerate(self, speed):
        if self.engine:
            self.speed = min(self.speed + speed, self.max_speed)
            print('Speed: {}'.format(self.speed))
        else:
            print('Engine is not started')

    def decelerate(self, speed):
        self.speed = max(self.speed - speed, 0)
        print('Speed: {}'.format(self.speed))


bmw = Auto("BMW", 200)
peugeot = Auto("Peugeot", 160)
fiat = Auto("Fiat", 140)
audi = Auto("Audi", 200)

peugeot.accelerate(100)
# Auto.accelerate(peugeot, 100) to samo co u góry, tutaj przekazujemy selfa,a w zapisie wyzej jest syntatic sugar
peugeot.start_engine()
peugeot.accelerate(100)
peugeot.accelerate(100)
peugeot.accelerate(100)
peugeot.decelerate(100)
peugeot.decelerate(100)
peugeot.decelerate(500)
peugeot.stop_engine()
