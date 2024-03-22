#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)

def convertirEnteros(lista):
    nuevaLista = []
    for elemento in lista:
        try:
            nuevoElemento = int(elemento)
        except ValueError:
            nuevoElemento = elemento
        nuevaLista.append(nuevoElemento)
    return tuple(nuevaLista)
          
t1 = input().split()
t2 = input().split()

t1 = convertirEnteros(t1)
t2 = convertirEnteros(t2)

print(t2+t1+t2)
