from point import Point
from triangle import Triangle, Isosceles, Equilateral, Scalene
from rectangle import Rectangle
from square import Square
from shape import Shape

def test_shape_package():
    print("===== PRUEBAS DEL PAQUETE SHAPE =====\n")

    try:
        print("---- TRIÁNGULOS ----")
        p1, p2, p3 = Point(0, 0), Point(4, 0), Point(2, 3)
        t = Triangle(p1, p2, p3)
        print("Área triángulo:", round(t.compute_area(), 2))
        print("Perímetro triángulo:", round(t.compute_perimeter(), 2))

        iso = Isosceles(Point(0,0), Point(2,0), Point(1,3))
        print("Isósceles regular:", iso.get_is_regular())

        eq = Equilateral(Point(0,0), Point(2,0), Point(1,1.732))
        print("Equilátero regular:", eq.get_is_regular())

        sc = Scalene(Point(0,0), Point(4,0), Point(3,2))
        print("Escaleno regular:", sc.get_is_regular())

    except Exception as e:
        print("Error en triángulos:", e)

    print("\n---- RECTÁNGULOS ----")
    try:
        p1, p2 = Point(0, 0), Point(4, 3)
        rect = Rectangle(corner1=p1, corner2=p2)
        print("Área rectángulo:", rect.compute_area())
        print("Perímetro rectángulo:", rect.compute_perimeter())
    except Exception as e:
        print("Error en rectángulos:", e)

    print("\n---- CUADRADOS ----")
    try:
        sq = Square(Point(2, 2), 4)
        print("Área cuadrado:", sq.compute_area())
        print("Perímetro cuadrado:", sq.compute_perimeter())
    except Exception as e:
        print("Error en cuadrados:", e)

    print("\n---- PRUEBAS DE EXCEPCIONES ----")
    try:
        print("Intentando crear un rectángulo sin argumentos...")
        r = Rectangle()
    except Exception as e:
        print("Excepción capturada:", e)

    try:
        print("\nIntentando asignar vértices no válidos...")
        s = Shape()
        s.set_vertices([1, 2, 3])  # no son objetos Point
    except Exception as e:
        print("Excepción capturada:", e)

    try:
        print("\nIntentando asignar ángulos con valores no numéricos...")
        s = Shape()
        s.set_inner_angles(["a", "b", "c"])
    except Exception as e:
        print("Excepción capturada:", e)

    try:
        print("\nIntentando establecer regularidad con valor no booleano...")
        s = Shape()
        s.set_is_regular("sí")
    except Exception as e:
        print("Excepción capturada:", e)

if __name__ == "__main__":
    test_shape_package()
