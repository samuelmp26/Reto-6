from shape import Shape
from line import Line
from point import Point 

class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        # Valido puntos
        for p in (p1, p2, p3):
            if not isinstance(p, Point):
                raise TypeError("Todos los vértices deben ser instancias de Point.")
        if p1 == p2 or p2 == p3 or p1 == p3:
            raise ValueError("Los vértices de un triángulo deben ser distintos.")
        super().__init__()
        self.vertices = [p1, p2, p3]
        self.edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]

    def compute_perimeter(self):
        return sum(line.length for line in self.edges)

    def compute_area(self):
        # Compruebo que no sean colineales (área cero)
        a, b, c = [line.length for line in self.edges]
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c))
        if area <= 0:
            raise ValueError("Los puntos no forman un triángulo válido (colineales).")
        return area**0.5


class Isosceles(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        lengths = [line.length for line in self.edges]
        self.is_regular = len(set(round(l,5) for l in lengths)) <= 2


class Equilateral(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        lengths = [line.length for line in self.edges]
        self.is_regular = len(set(round(l,5) for l in lengths)) == 1


class Scalene(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        lengths = [line.length for line in self.edges]
        self.is_regular = len(set(round(l,5) for l in lengths)) == 3


class TriRectangle(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
