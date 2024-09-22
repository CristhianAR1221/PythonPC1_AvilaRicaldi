#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:----
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de introducir una opción inválida, el programa informará de que no es correcta.

Num1 = int(input("Ingresar un numero "))
Num2 = int(input("Ingresar otro numero"))

print("Bienvenido al Menu, seleccione una de las siguientes opciones")
print("1. Suma")
print("2. Resta")
print("3. Producto")

Opcion= int(input("Seleccione una de las alternativas del menu "))
if Opcion == 1:
    op = Num1 + Num2
    print(op)
else:
    if Opcion == 2:
        op = abs(Num1 - Num2)
        print(op)
    else:
        if Opcion == 3:
            op = Num1*Num2
        else:
            while Opcion > 4:
                print("El numero ingresado no es correcto")
                Opcion = int(input("Ingrese el numero mostrado en el menu"))
                if Opcion == 1:
                    op = Num1 + Num2
                    print(op)
                else:
                    if Opcion == 2:
                        op = abs(Num1 - Num2)
                        print(op)
                    else:
                        op = Num1*Num2
                        print(op)
                
        
