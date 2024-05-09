import logging

logger = logging.getLogger(__name__)
my_format = '{msg}'
logging.basicConfig(filename='mylog_rectangle.log', filemode='a', encoding='UTF-8', level=logging.INFO, style = '{', format=my_format)
class Rectangle:
    def __init__(self, width: int, height:int):
        logger.info(msg = f'Высота: {width}, Ширина: {height}')
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                return Rectangle(self.width - other.width, self.height - other.height)
        else:
            raise TypeError

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self is other

    def __le__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f' Прямоугольник со сторонами{self.width}и{self.height}'
        raise TypeError
    def __repr__(self):
        return f' Rectangle{self.width},{self.height}'

w1 = int(input('Введите высоту первого прямоугольника: '))
h1 = int(input('Введите ширину первого прямоугольника: '))
w2 = int(input('Введите высоту второго прямоугольника: '))
h2 = int(input('Введите ширину второго прямоугольника: '))
rect1 = Rectangle(w1, h1)
rect2 = Rectangle(w2, h2)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")
