# Создайте абстрактный класс `Shape` с методом `area`,
# который будет возвращать площадь фигуры.
# Затем создайте два подкласса `Rectangle` и `Circle`,
# которые наследуют от `Shape` и переопределяют метод `area`
# для расчета площади прямоугольника и круга соответственно.
# Создайте объекты этих классов и вызовите метод `area` для каждого из них.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(pi * (self.__radius ** 2), 2)


rectangle = Rectangle(3, 8)
circle = Circle(4.6)

print(f"Площадь прямоугольника = {rectangle.area()}\n"
      f"Площадь круга = {circle.area()}")
