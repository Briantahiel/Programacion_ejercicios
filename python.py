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




import datetime

fecha_actual = datetime.datetime.now()
fecha = fecha_actual.strftime("%Y-%m-%d")
hora = fecha_actual.strftime("%H:%M:%S")

temp = float(input("Temperatura: "))
mensaje = ("Temp: " + str(temp) + "°C " + fecha + hora)
print(mensaje)




