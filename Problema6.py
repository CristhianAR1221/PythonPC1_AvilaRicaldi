#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

Edad = int(input("¿Cuantos años tienes? "))
print("Usted tiene " + str(Edad) + " años")
Entrada = 0
if Edad < 4 : 
    print("Ingresar de manera gratuita ")
else:
    if Edad < 18:
        Entrada = 5
        print("La entrada es " + str(Entrada) + " dolares")
    else:
        Entrada = 10
        print("La entrada es " + str(Entrada)+ " dolares")