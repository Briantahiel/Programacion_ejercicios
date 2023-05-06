import datetime
while True:
    try:
        fecha_nac = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
        fecha_nacimiento = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y").date()
        fecha_actual = datetime.date.today()
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if(fecha_actual.month, fecha_actual.day) == (fecha_nacimiento.month, fecha_nacimiento.day):
            print("Feliz Cumpleaños!. Cumpliste", edad, "años")
        else:    
            print("Usted tiene:", edad, "años")
    except ValueError:    
        print("Ingrese un formato válido")
