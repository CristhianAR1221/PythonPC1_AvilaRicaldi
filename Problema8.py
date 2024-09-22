#Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
#entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
#Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
#hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
#Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
#suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
#las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.

tiempo = str(input("Ingresar una hora "))
h,m = tiempo.split(":")
horas = int(h)
minutos = int(m)
if horas == 7:
    print("Hora de desayunar")
else:
    if horas == 8 and minutos == 00:
        print("Hora de desayunar")
    else:
        if horas == 12 :
            print("Hora de almorzar")
        else:
            if horas == 13 and minutos == 00:
                print("Hora de almorzar")
            else:
                if horas == 18 :
                    print("Hora de cenar")
                else:
                    if horas == 19 and minutos == 00:
                        print("Hora de cenar")