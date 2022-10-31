# auto - brand, speed, max_speed, engine


def auto_factory(brand, max_speed):
    return {
        'brand': brand,
        'speed': 0,
        'max_speed': max_speed,
        'engine': False
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('Engine started')
    else:
        print('Engine already started')


def stop_engine(car):
    car['engine'] = False
    print('Engine stopped')


def accelerate(car, speed):
    if car['engine']:
        car['speed'] = min(car['speed'] + speed, car['max_speed'])
        print('Speed: {}'.format(car['speed']))
    else:
        print('Engine is not started')


def decelerate(car, speed):
    car['speed'] = max(car['speed'] - speed, 0)
    print('Speed: {}'.format(car['speed']))


bmw = auto_factory('BMW', 200)

accelerate(bmw, 100)
start_engine(bmw)
accelerate(bmw, 100)
accelerate(bmw, 100)
accelerate(bmw, 100)
decelerate(bmw, 100)
decelerate(bmw, 100)
decelerate(bmw, 500)
stop_engine(bmw)
