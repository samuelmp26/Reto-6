class Shape:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.inner_angles = []
        self.is_regular = False

    def set_vertices(self, vertices):
        # Valido que la lista contenga objetos tipo Point
        if not all(hasattr(v, "x") and hasattr(v, "y") for v in vertices):
            raise TypeError("Todos los vértices deben ser objetos de tipo Point.")
        self.vertices = vertices

    def get_vertices(self):
        return self.vertices

    def set_edges(self, edges):
        # Valido que los bordes sean líneas
        if not all(hasattr(e, "length") for e in edges):
            raise TypeError("Todos los bordes deben ser objetos de tipo Line.")
        self.edges = edges

    def get_edges(self):
        return self.edges

    def set_inner_angles(self, angles):
        # Valido que los ángulos sean numéricos
        if not all(isinstance(a, (int, float)) for a in angles):
            raise TypeError("Los ángulos deben ser valores numéricos.")
        self.inner_angles = angles

    def get_inner_angles(self):
        return self.inner_angles

    def set_is_regular(self, regular):
        if not isinstance(regular, bool):
            raise TypeError("El atributo de regularidad debe ser booleano.")
        self.is_regular = regular

    def get_is_regular(self):
        return self.is_regular

    def compute_area(self):
        return 0

    def compute_perimeter(self):
        return 0

    def compute_inner_angles(self):
        return []
