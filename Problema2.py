#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

Consumo= int(input("¿Cuanto fue su consumo?"))
Porcentaje=int(input("¿Que porcentaje de su consumo le quiere dar al mesero por su servicio?( Considerar que debe ser mayor o igual a 15%)"))
while Porcentaje < 15:
    print("El porcentaje por ley norteameticana debe ser superior o igual a 15, introduzca nuevamente el valor del porcentaje")
    Porcentaje=int(input("¿Que porcentaje de su consumo le dara al mesero por su servicio?"))
Propina = float((Consumo*Porcentaje)/100)
print("La propina del mesero será " + str(Propina))


