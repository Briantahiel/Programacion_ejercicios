# def sum(num1, num2):
#     suma = num1 + num2
#     return suma
# while True:
#     try: 
#         num1 = float(input("1° Número: "))
#         num2 = float(input("2° Número: "))
#         break
#     except ValueError:
#         print("Valor incorrecto")
# print(sum(num1, num2))


# 1. En un laboratorio se toman medidas de temperatura de una substancia cada una
# hora, y se anota la hora y la temperatura en una planilla. Hacer un algoritmo que
# tome la mayor temperatura y la menor temperatura y a que hora se produjo.

# import datetime
# fecha_actual = datetime.datetime.now()
# fecha = fecha_actual.strftime("%Y-%m-%d")
# hora = fecha_actual.strftime("%H:%M:%S")
# list_temp = []
# while True: 
#     temp_str = input("Temperatura o 'parar': ")
#     if temp_str.lower() == 'parar':
#         break
#     try:
#         temp = float(temp_str)
#     except ValueError:
#         print("Ingrese un valor numérico válido.")
#         continue
#     list_temp.append(temp)
# temp_mayor = max(list_temp)
# mensaje = ("Temp máx: " + str(temp_mayor) + "°C " + fecha + hora)
# print(mensaje)
# print(list_temp)


# 2. Hacer un algoritmo que cuente cuantos múltiplos de 3 hay entre x y z.
# count = 0
# num1 = int(input("Desde: "))
# num2 = int(input("Hasta: "))
# if(num1 < num2):
#    for i in range(num1, num2):  
#     if(i % 3 == 0):
#         count += 1
#     print("Hay " + str(count) + " múltiplos de 3.")  
# else:
#     print("Error!")  

# 3. Hacer un algoritmo que me permita ingresar un número y que aparezca el
# nombre de una provincia, tomando en cuenta la cantidad de provincias
# argentinas que existen para poder validar.

# provincias = ["Buenos Aires","Córdoba",
#   "Santa Fe","Mendoza","Tucumán","Entre Ríos","Salta","Chaco","Corrientes"
#   ,"Misiones","San Juan","Jujuy","Río Negro","Neuquén","Formosa","Chubut"
#   ,"San Luis","La Rioja", "Santiago del Estero","Catamarca","La Pampa","Santa Cruz","Tierra del Fuego"]

# while True:
#     try:
#         num = int(input("Ingrese un núm del 1 al 23: "))
#         if(num >= 1 and num <=23):
#             eleccion = provincias[num - 1]
#             print(eleccion)     
#     except ValueError:
#         print("Ingrese un número válido")

# import time

# corredores = []
# vuelta = 1
# inicio_carrera = time.time()
# hora = time.strftime("%H:%M:%S")
# print(f"La carrera ha iniciado en {hora}")

# print(float(inicio_carrera) - float(hora))


import time

corredores = []
vuelta = 1
inicio_carrera = time.time()
hora = time.strftime("%H:%M:%S")
print(f"La carrera ha iniciado en {hora}")

while vuelta <= 6:
    # print(f"\nVuelta {vuelta}")
    for i in range(1, 6):
        corredor = input("Nombre: ")
        tiempo_vuelta = time.time() - inicio_carrera
        corredores.append({corredor: {vuelta: inicio_carrera}})
        break
    encontrado = False
    for cor in corredores:
        if corredor in cor:
            vuelta += 1
            encontrado = True
        #         break
        # if not encontrado:
        #     for cor in corredores:
        #         if corredor in cor:
        #             cor[corredor][vuelta] = tiempo_vuelta
        #             encontrado = True
        #             break
        #     if not encontrado:
        #         corredores.append({corredor: {vuelta: tiempo_vuelta}})
        # print(corredores)
    vuelta += 1        
print(corredores)





# for i in range(1, 4):
#     corredor = input("Ingrese nombre del corredor: ")

#     encontrado = False
#     for dic in corredores:
#         if corredor in dic:
#             tiempo_vuelta = time.time() - inicio_carrera
#             dic[corredor][vuelta] = tiempo_vuelta
#             vuelta += 1
#             encontrado = True
#             break
#     if not encontrado:
#         corredores.append({corredor: {vuelta: time.time() - inicio_carrera}})
    
   
# print(corredores)


