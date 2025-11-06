class Point:
    def __init__(self, x=0, y=0):
        # Valido que los valores sean numéricos
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Las coordenadas de un punto deben ser numéricas.")
        self.x = x
        self.y = y

    def set_x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("El valor de x debe ser numérico.")
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError("El valor de y debe ser numérico.")
        self.y = y

    def get_y(self):
        return self.y

    def compute_distance(self, point):
        # Valido que el argumento sea un objeto Point
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de Point.")
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
