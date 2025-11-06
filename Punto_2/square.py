from rectangle import Rectangle
from point import Point

class Square(Rectangle):
    def __init__(self, center_point, side):
        # Valido tipo y valor
        if not isinstance(center_point, Point):
            raise TypeError("El punto central debe ser una instancia de Point.")
        if side <= 0:
            raise ValueError("El lado del cuadrado debe ser positivo.")
        x = center_point.x - side/2
        y = center_point.y - side/2
        bottom_left = Point(x, y)
        super().__init__(bottom_left=bottom_left, width=side, height=side)
        self.is_regular = True

    def compute_area(self):
        return self.width ** 2

    def compute_perimeter(self):
        return 4 * self.width
