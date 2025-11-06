if __name__ == '__main__':
    print("Ingrese 2 valores para ser operados:")
try:
    a = int(input())
    b = int(input())
except ValueError:
    print("Error: Debe ingresar solo números enteros.")
    exit()   
class Calculadora:
    def sumar (a, b):
        return a + b
    def restar (a, b):
        return a - b 
    def multiplicar (a, b):
        return a * b
    def dividir (a, b):
        try:
            return a / b 
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            return None
print("Elija la operacion a realizar:")
print("Suma: 1\nResta: 2\nMultiplicacion: 3\nDivision: 4")
try:
    operacion = int(input())
except ValueError:
    print("Error: Debe ingresar un número entre 1 y 4.")
    exit()
class Seleccion_Operacion:
    def operacion():
        if operacion == 1:
            print("El resultado es", Calculadora.sumar(a, b))
        elif operacion == 2:
            print("El resultado es", Calculadora.restar(a, b))
        elif operacion == 3:
            print("El resultado es", Calculadora.multiplicar(a, b))
        elif operacion == 4:
            resultado = Calculadora.dividir(a, b)
            if resultado is not None:
                print("El resultado es", resultado)
        else:
            print("Operacion no valida")
    
Seleccion_Operacion.operacion()
