#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:

NumeroEntero = int(input("Introduzca el ultimo numero de una serie de sumatoria: "))
i = 1
Suma = 1
while i != NumeroEntero:
    i = i+1
    Suma = Suma + i
print("La sumatoria total es " + str(Suma))

