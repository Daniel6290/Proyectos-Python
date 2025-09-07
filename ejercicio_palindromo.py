#Verificar una cadena de numeros a ver si cumple con el algoritmo de luhn

def luhn(numero):
#eliminar los espacios de los numeros
    numero = numero.replace("", "")
#Solo debe contener numeros
    if not numero.isdigit():
        return False
    
    num_invertido = numero[::-1]

    sum_t = 0
#Pasar por los digitos

    for i in range(len(num_invertido)):
        digit = int(num_invertido[i])

#Duplicar los digitos en posiciones inpares
#Si el resultado es mayor a nueve se le resta 9
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        sum_t += digit
    
    return sum_t % 10 == 0

numero = input("Porfavor digite el numero que desea verificar con luhn: ")

if luhn(numero):
    print("El numero cumple con el algoritmo")
else:
    print("El numero no cumple con el algorito")



    
    



