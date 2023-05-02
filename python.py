# 4. En una carrera de bicicletas hay 35 corredores, por cada vuelta se toma el
# nombre del corredor, el puesto en el que está en ese momento y el tiempo que
# tardó en dar la vuelta, la carrera es a 50 vueltas, tomar mejor vuelta y que
# corredor la hizo.


import time

corredores = []
vuelta = 1
inicio_carrera = time.time()
hora = time.strftime("%H:%M:%S")
print(f"La carrera ha iniciado en {inicio_carrera}")

while vuelta <= 2:
    print(f"\nVuelta {vuelta}")
    for corredor in range(1, 3):
        nombre = input("Nombre: ")
        tiempo_vuelta = time.time() - inicio_carrera
        corredores.append({"nombre": nombre, "vuelta": vuelta, "tiempo": tiempo_vuelta})
     
    mejor_tiempo_vuelta = min([corredor["tiempo"] for corredor in corredores if corredor["vuelta"] == vuelta])
    nombre_mejor_tiempo = [corredor["nombre"] for corredor in corredores if corredor["tiempo"] == mejor_tiempo_vuelta][0]
    print("Mejor tiempo para la vuelta", vuelta, nombre_mejor_tiempo, mejor_tiempo_vuelta)

    vuelta += 1

print(corredores)

def sum(num1, num2):
    suma = num1 + num2
    return suma
while True:
    try: 
        num1 = float(input("1° Número: "))
        num2 = float(input("2° Número: "))
        break
    except ValueError:
        print("Valor incorrecto")
print(sum(num1, num2))


# 1. En un laboratorio se toman medidas de temperatura de una substancia cada una
# hora, y se anota la hora y la temperatura en una planilla. Hacer un algoritmo que
# tome la mayor temperatura y la menor temperatura y a que hora se produjo.

import datetime
fecha_actual = datetime.datetime.now()
fecha = fecha_actual.strftime("%Y-%m-%d")
hora = fecha_actual.strftime("%H:%M:%S")
list_temp = []
while True: 
    temp_str = input("Temperatura o 'parar': ")
    if temp_str.lower() == 'parar':
        break
    try:
        temp = float(temp_str)
    except ValueError:
        print("Ingrese un valor numérico válido.")
        continue
    list_temp.append(temp)
temp_mayor = max(list_temp)
mensaje = ("Temp máx: " + str(temp_mayor) + "°C " + fecha + hora)
print(mensaje)
print(list_temp)


# 2. Hacer un algoritmo que cuente cuantos múltiplos de 3 hay entre x y z.
count = 0
num1 = int(input("Desde: "))
num2 = int(input("Hasta: "))
if(num1 < num2):
   for i in range(num1, num2):  
    if(i % 3 == 0):
        count += 1
    print("Hay " + str(count) + " múltiplos de 3.")  
else:
    print("Error!")  



# 3. Hacer un algoritmo que me permita ingresar un número y que aparezca el
# nombre de una provincia, tomando en cuenta la cantidad de provincias
# argentinas que existen para poder validar.

provincias = ["Buenos Aires","Córdoba",
  "Santa Fe","Mendoza","Tucumán","Entre Ríos","Salta","Chaco","Corrientes"
  ,"Misiones","San Juan","Jujuy","Río Negro","Neuquén","Formosa","Chubut"
  ,"San Luis","La Rioja", "Santiago del Estero","Catamarca","La Pampa","Santa Cruz","Tierra del Fuego"]

while True:
    try:
        num = int(input("Ingrese un núm del 1 al 23: "))
        if(num >= 1 and num <=23):
            eleccion = provincias[num - 1]
            print(eleccion)     
    except ValueError:
        print("Ingrese un número válido")


import datetime

# Fecha de nacimiento de ejemplo: 1 de enero de 1990
fecha_nacimiento = datetime.date(1990, 1, 1)

# Fecha actual
fecha_actual = datetime.date.today()

# Cálculo de la edad en años
edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Imprimir la edad
print("La edad es:", edad, "años")

