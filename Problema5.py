#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False  - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

Nshow= int(input("¿Cuantos shows musicales ha visto en este ultimo año? "))
if Nshow < 3 :
    Valor = False
else:
    Valor = True
print(Valor)