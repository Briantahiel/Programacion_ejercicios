import os

while True:
    print("Ingrese un número del 1 al 4:")
    print("1. Limpiar la pantalla de la consola (cls)")
    print("2. Listar archivos y directorios (dir)")
    print("3. Crear un directorio (mkdir)")
    print("4. Listar archivos y directorios de forma detallada (dir /w)")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == '1':
        os.system('cls')
    elif opcion == '2':
        os.system('dir')
    elif opcion == '3':
        nombre_directorio = input("Ingrese el nombre del directorio a crear: ")
        os.system(f'mkdir {nombre_directorio}') 
    elif opcion == '4':
        os.system('dir /w') 
    elif opcion == '0':
        break  
    else:
        print("Opción inválida. Intente nuevamente.")
