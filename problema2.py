#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)

def convertirEnteros(lista):
    nuevaLista = []
    for elemento in lista:
        try:
            nuevoElemento = int(elemento)
        except ValueError:
            nuevoElemento = elemento
        nuevaLista.append(nuevoElemento)
    return tuple(nuevaLista)

t = input().split()

t = convertirEnteros(t)

print(t[::-1])
