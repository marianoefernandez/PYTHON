from data import lista_bzrp
'''


[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
'''

#Funciones

def ImprimirKeys(lista,keys):
    for elemento in lista:
        print("\n")
        for key in keys:
            print("{0}:{1}".format(key,elemento[key]))

def menu(lista_bzrp):

    respuesta = True

    while(respuesta):
        print("1-Imprimir títulos\n2-Tema más visto y su cantidad\n3-Tema menos visto y su cantidad",
        "\n4-Tema más largo\n5-Tema más corto\n6-Duración promedio de temas",
        "\n7-Promedio de vistas\n8-Cantidad de reproducciones del canal\n9-Salir")

        opcion = input("Su opcion:")

        while(not opcion.isnumeric()):
            opcion = input("ERROR/Sólo se permiten números\nSu opcion:")

        opcion = int(opcion)

        match(opcion):
            case 1:
                print("Imprimo títulos y cantidad de reproducciones")
                ImprimirKeys(lista_bzrp,["title","views"])
            case 2:
                print("2")
            case 3:
                print("3")
            case 4:
                print("4")
            case 5:
                print("5")
            case 6:
                print("6")
            case 7:
                print("7")
            case 8:
                print("8")
            case 9:
                print("9")
                respuesta = False
            case other:
                print("Número incorrecto (Sólo entre 1-9)")

#Desarrollo

menu(lista_bzrp)