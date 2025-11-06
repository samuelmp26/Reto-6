if __name__ == '__main__':
    print("Ingrese las palabras separadas por espacio:")
    entrada = input()
    lista = entrada.split()
if not lista:
    raise ValueError("Error: No se ingresaron palabras.")
for palabra in lista:
    if not palabra.isalpha():
        raise ValueError(f"Error: '{palabra}' contiene caracteres no válidos.")
class Palabras:
    def agrupar(lista):
        grupos = {}
        for palabra in lista:
            clave = ''.join(sorted(palabra))
            if clave not in grupos:
                grupos[clave] = [palabra]
            else:
                grupos[clave].append(palabra)
        resultado = []
        for clave in grupos:
            if len(grupos[clave]) > 1:
                resultado.append(grupos[clave])
        return resultado
class Seleccion_Palabras:
    def mostrar():
        resultado = Palabras.agrupar(lista)
        if len(resultado) > 0:
            print("Grupos encontrados:")
            for grupo in resultado:
                print(grupo)
        else:
            print("No se encontraron grupos")
Seleccion_Palabras.mostrar()
