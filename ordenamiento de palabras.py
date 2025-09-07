#Funcion para ordenar una lista de palabras y las ordene alfabeticamente

def ordenamiento(lista):

    palabra = len(lista)
# Detectar si ya está ordenado, comprobar si los últimos i elementos ya están en su lugar

    for i in range(palabra):
        intercambiado = False
# Comparamos elementos adyacentes y Intercambiamos si están en el orden incorrecto
# Se ponen las palabras en minuscula para poder comparar mejor
        for j in range(0, palabra -i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
            
    return lista

palabras = ["banana", "perro", "pera", "uva", "zebra", "bolos", "arbol", "avion"]

print("Lista original: ", palabras)
list_ordenada = ordenamiento(palabras)

print("lista ordenada: ",list_ordenada)