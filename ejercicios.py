# Consigna: aplicar al código un
# while para poder salir del programa cuando el
# operador lo disponga. While true

colores = ["Rojo", "Negro", "Blanco"]

while True:
    number = input("Ingrese un núm del 1 al 3 o salir: ")
    if number.lower() == 'salir':
        break
    try:
        num = int(number)
        if(num >= 1 and num <=3):
            eleccion = colores[num - 1]
            print(eleccion)
        else:
            print("Valor fuera del rango")     
    except ValueError:
        print("Ingrese un número válido")