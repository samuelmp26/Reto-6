from shape import Shape
from line import Line
from point import Point

class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__()
        # Valido que los argumentos sean correctos
        if "bottom_left" in kwargs and "width" in kwargs and "height" in kwargs:
            bottom_left = kwargs["bottom_left"]
            width = kwargs["width"]
            height = kwargs["height"]
            if not isinstance(bottom_left, Point):
                raise TypeError("bottom_left debe ser una instancia de Point.")
            if width <= 0 or height <= 0:
                raise ValueError("El ancho y la altura deben ser positivos.")
            p1 = bottom_left
            p2 = Point(bottom_left.x + width, bottom_left.y)
            p3 = Point(bottom_left.x + width, bottom_left.y + height)
            p4 = Point(bottom_left.x, bottom_left.y + height)
            self.vertices = [p1, p2, p3, p4]
        elif "corner1" in kwargs and "corner2" in kwargs:
            corner1 = kwargs["corner1"]
            corner2 = kwargs["corner2"]
            if not isinstance(corner1, Point) or not isinstance(corner2, Point):
                raise TypeError("corner1 y corner2 deben ser instancias de Point.")
            if corner1.x == corner2.x or corner1.y == corner2.y:
                raise ValueError("Los puntos no pueden formar un rectángulo válido.")
            self.vertices = [corner1, Point(corner2.x, corner1.y), corner2, Point(corner1.x, corner2.y)]
        else:
            raise ValueError("Argumentos inválidos para inicializar el rectángulo")

        self.edges = [Line(self.vertices[i], self.vertices[(i+1)%4]) for i in range(4)]
        self.width = self.edges[0].length
        self.height = self.edges[1].length

    def set_width(self, w):
        if w <= 0:
            raise ValueError("El ancho debe ser un número positivo.")
        self.width = w

    def get_width(self):
        return self.width

    def set_height(self, h):
        if h <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        self.height = h

    def get_height(self):
        return self.height

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)
