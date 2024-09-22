#Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
#'día', 'buen', 'Di'].

Lista = list(input("Ingrese una frase "))
Inv = Lista[::-1]
print("La lista invertida es " + str(Inv))