CANTIDAD_EMPLEADOS = 3

lista_empleados = []

for i in range(CANTIDAD_EMPLEADOS):
    empleado = {"nombre":"","apellido":"","dni":0}

    for key in empleado:
        empleado[key] = input("Ingrese {0}: ".format(key))
    
    lista_empleados.append(empleado)

i = 0
for empleado in lista_empleados:
    print("[{0}] {1} - {2} - {3}".format(i,empleado["nombre"],empleado["apellido"], empleado["dni"]))
    i = i + 1
