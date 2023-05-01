colores = ["Rojo", "Negro", "Blanco"]

while True:
    try:
        num = int(input("Ingrese un núm del 1 al 3: "))
        if(num >= 1 and num <=3):
            eleccion = colores[num - 1]
            print(eleccion)     
    except ValueError:
        print("Ingrese un número válido")