"""
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total
"""

contador_barbijos = 0
acumulador_jabones = 0
flag = False

for i in range(5):
    tipo = input("Ingrese el tipo ")
    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("ERROR/ Reingrese el tipo" )
    
    precio = input("Ingrese el precio (Entre 100 y 300) ")
    precio = float(precio)
    while(precio < 100 or precio > 300):
        precio = input("ERROR/ Por favor ingrese un NUMERO entre el 100 y 300 ")
        precio = float(precio)

    cantidad_unidades = input("Ingrese la cantidad de unidades (No mayor a 1000)")
    cantidad_unidades = int(cantidad_unidades)
    while(cantidad_unidades < 1 or cantidad_unidades > 1000):
        cantidad_unidades = input("ERROR/ Por favor ingrese un NUMERO entre el 1 y 1000")
        cantidad_unidades = int(cantidad_unidades)

    marca = input("Ingrese la marca")
    fabricante = input("Ingrese el fabricante")

    if(tipo == "barbijo" and (flag == False or precio > barbijo_mas_caro)):
        barbijo_mas_caro = precio
        cantidad_unidades_mas_caro = cantidad_unidades
        fabricante_mas_caro = fabricante
        contador_barbijos += 1
        flag = True

    if(i == 0 or cantidad_unidades_maxima < cantidad_unidades):
        cantidad_unidades_maxima = cantidad_unidades
        fabricante_mas_unidades = fabricante

    if(tipo == "jabon"):
        acumulador_jabones += cantidad_unidades
    
if(contador_barbijos):
    print("A-El más caro de los barbijos tiene una cantidad de ", cantidad_unidades_mas_caro, " unidades y es fabricado por: ",fabricante_mas_caro)
else:
    print("A-No se dio de alta ningun barbijo")

print("B-El item con más unidades es fabricado por: ",fabricante_mas_unidades, " y fabrico ", cantidad_unidades_maxima)
    
print("C- Hay" , acumulador_jabones , " de jabones.")



    

