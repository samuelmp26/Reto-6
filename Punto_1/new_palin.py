if __name__ == '__main__':
    print("Ingrese una palabra:")
    palabra = input().lower()
if not palabra:
    raise ValueError("Error: No ingresó ninguna palabra.")
if not palabra.isalpha():
    raise ValueError("Error: Solo se permiten letras sin espacios ni números.")
class Palabra:
    def es_palindromo(palabra):
        cantidad = len(palabra)
        es_palabra_palindromo = True
        for i in range(cantidad):
            j = cantidad - 1 - i
            if i < j:
                if palabra[i] != palabra[j]:
                    es_palabra_palindromo = False
        if es_palabra_palindromo == True:
            return True
        else:
            return False
class Seleccion_Palindromo:
    def mostrar():
        if Palabra.es_palindromo(palabra):
            print("La palabra es un palindromo")
        else:
            print("La palabra no es un palindromo")
Seleccion_Palindromo.mostrar()
