if __name__ == '__main__':
    print("Ingrese los numeros separados por espacio:")
    entrada = input()
try:
    lista = [int(x) for x in entrada.split()]
except ValueError:
    print("Error: Ingrese solo números enteros.")
    exit()
if len(lista) < 2:
    raise ValueError("Error: Debe ingresar al menos dos números.")
class Numeros:
    def mayor_suma(lista):
        if len(lista) < 2:
            return None
        mayor = lista[0] + lista[1]
        for i in range(len(lista) - 1):
            suma = lista[i] + lista[i + 1]
            if suma > mayor:
                mayor = suma
        return mayor
class Seleccion_Suma:
    def mostrar():
        resultado = Numeros.mayor_suma(lista)
        if resultado is not None:
            print("La mayor suma consecutiva es:", resultado)
        else:
            print("La lista debe tener al menos 2 numeros")
Seleccion_Suma.mostrar()
