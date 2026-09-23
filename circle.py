import math


def area(r):
    '''
    Возвращает площадь круга с радиусом r
        area(r)
    Параметры
        r (int): радиус круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с радиусом r
        perimeter(r)
    Параметры
        r (int): радиус круга
    '''
    return 2 * math.pi * r