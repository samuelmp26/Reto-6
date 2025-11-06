from point import Point

class Line:
    def __init__(self, start_point, end_point):
        # Verifico que los extremos sean puntos válidos
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Los extremos de la línea deben ser instancias de Point.")
        if start_point.x == end_point.x and start_point.y == end_point.y:
            raise ValueError("Una línea no puede tener extremos coincidentes.")
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)

    def set_start(self, point):
        if not isinstance(point, Point):
            raise TypeError("El punto inicial debe ser una instancia de Point.")
        self.start_point = point

    def get_start(self):
        return self.start_point

    def set_end(self, point):
        if not isinstance(point, Point):
            raise TypeError("El punto final debe ser una instancia de Point.")
        self.end_point = point

    def get_end(self):
        return self.end_point

    def get_length(self):
        return self.length
