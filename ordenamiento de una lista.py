#Funcion para ordenar una lista de forma gradual
#La ultima posicion de la lista tiene que ser el mayor de los numeros

def ordenamiento(lista):

    numero = len(lista)
# Detectar si ya está ordenado, comprobar si los últimos i elementos ya están en su lugar

    for i in range(numero):
        intercambiado = False
# Comparamos elementos adyacentes y Intercambiamos si están en el orden incorrecto
        for j in range(0, numero -i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
            
    return lista

mi_lista = [64, 34, 25, 12, 22, 11, 90]

lista_ordenada = ordenamiento(mi_lista)

print("Lista ordenada:", lista_ordenada)