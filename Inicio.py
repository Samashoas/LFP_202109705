from colorama import Fore
import tkinter as tk
from tkinter import filedialog
from Procesos import CargaArc, ProcPeliculas

MoviesList = ProcPeliculas()

def MenuCargaArchivo():
    print(Fore.GREEN+'¿Ingresar otros datos?')
    print('1. Si')
    print('2. No')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))
    if option == 1:
        cargarArchivos()
    elif option == 2:
        menu()
    else:
        print("opcion invalida")
        print()
        MenuCargaArchivo()
        option = int(input("Seleccione una opción: "))

def menuMostrarPeli():
    print(Fore.GREEN+'¿Regresar al menu principal?')
    print('1. Si')
    print('2. No, regresar a la pestaña anterior solamente')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))
    if option == 1:
        menu()
    elif option == 2:
        GestionDatos()
    else:
        print("opcion invalida")
        print()
        menuMostrarPeli()
        option = int(input("Seleccione una opción: "))

def menuMostrarPeliAct():
    print(Fore.GREEN+'¿Ingresar otro dato?')
    print('1. Si')
    print('2. No, regresar a la pestaña anterior solamente')
    print('3. No, regresar al menu principal')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))
    if option == 1:
        option = (input(Fore.GREEN +"Ingrese una pelicula: "))
        for i in MoviesList.MoviesList:
            if option == i.pelicula:
                print(i.actor)
        menuMostrarPeliAct()
    elif option == 2:
        GestionDatos()
    elif option == 3:
        menu()
    else:
        print("opcion invalida")
        print()
        menuMostrarPeli()
        option = int(input("Seleccione una opción: "))

def MenuFiltradoActor():
    print(Fore.GREEN+'¿Ingresar otro dato?')
    print('1. Si')
    print('2. No, regresar a la pestaña anterior solamente')
    print('3. No, regresar al menu principal')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))
    if option == 1:
        option = (input(Fore.GREEN +"Ingrese un actor: "))
        for i in MoviesList.Factorio(option):
            print(Fore.BLUE + i.pelicula)
        MenuFiltradoActor()
    elif option == 2:
        FiltradoDatos()
    elif option == 3:
        menu()
    else:
        print("opcion invalida")
        print()
        menuMostrarPeli()
        option = int(input("Seleccione una opción: "))

def MenuFiltradoYear():
    print(Fore.GREEN+'¿Ingresar otro dato?')
    print('1. Si')
    print('2. No, regresar a la pestaña anterior solamente')
    print('3. No, regresar al menu principal')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))
    if option == 1:
        option = (input(Fore.GREEN +"Ingrese un año: "))
        for i in MoviesList.Anotorio(option):
            print(Fore.BLUE + i.pelicula)
        MenuFiltradoActor()
    elif option == 2:
        FiltradoDatos()
    elif option == 3:
        menu()
    else:
        print("opcion invalida")
        print()
        menuMostrarPeli()
        option = int(input("Seleccione una opción: "))

def MenuFiltradoGen():
    print(Fore.GREEN+'¿Ingresar otro dato?')
    print('1. Si')
    print('2. No, regresar a la pestaña anterior solamente')
    print('3. No, regresar al menu principal')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))
    if option == 1:
        option = (input(Fore.GREEN +"Ingrese un genero: "))
        for i in MoviesList.Genotorio(option):
            print(Fore.BLUE + i.pelicula)
        MenuFiltradoActor()
    elif option == 2:
        FiltradoDatos()
    elif option == 3:
        menu()
    else:
        print("opcion invalida")
        print()
        menuMostrarPeli()
        option = int(input("Seleccione una opción: "))

def cargarArchivos():
    file_path = filedialog.askopenfilename(title="Selecciona un documento", filetypes=[("Documentos tipo LFP", ".lfp")])
    abrir = open(file_path, 'r')

    try:
        for i in abrir.read().split('\n'):
            divList = i.split(';')
            try:
                NM = CargaArc(divList[0], divList[1].split(','), divList[2], divList[3])
                MoviesList.Pelicutorio(NM)
            except Exception as error:
                print(error)
        for i in MoviesList.MoviesList:
            print(i)   
    except Exception as error:
        print(error)
    finally:
        abrir.close()
    MenuCargaArchivo()
        
def GestionDatos():
    print(Fore.CYAN +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('|                    1. Mostrar peliculas           |')
    print('*                    2. Mostrar Actores             *')
    print('|                    3. Menu principal              |')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))  
    if option == 1:
        for i in MoviesList.MoviesList:
            print(Fore.CYAN + i.pelicula)
        menuMostrarPeli()
    elif option == 2:
        option = (input(Fore.GREEN +"Ingrese una pelicula: "))
        for i in MoviesList.MoviesList:
            if option == i.pelicula:
                print(i.actor)
        menuMostrarPeliAct()
    elif option == 3:
        menu()
    else:
        print("opcion invalida")
        print()
        GestionDatos()
        option = int(input("Seleccione una opción: "))

def FiltradoDatos():
    print(Fore.MAGENTA +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('|                    1. Filtrado por actor          |')
    print('*                    2. Filtrado por año            *')
    print('|                    3. Filtrado por genero         |')
    print('|                    4. Menu principal              |')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))  
    if option == 1:
        option = (input(Fore.GREEN +"Ingrese un actor: "))
        for i in MoviesList.Factorio(option):
            print(Fore.BLUE + i.pelicula)
        MenuFiltradoActor()
    elif option == 2:
        option = (input(Fore.GREEN +"Ingrese un año: "))
        for i in MoviesList.Anotorio(option):
            print(Fore.BLUE + i.pelicula)
        MenuFiltradoYear()
    elif option == 3:
        option = (input(Fore.GREEN +"Ingrese un genero: "))
        for i in MoviesList.Genotorio(option):
            print(Fore.BLUE + i.pelicula)
        MenuFiltradoGen()
    elif option == 4:
        menu()
    else:
        print("opcion invalida")
        print()
        FiltradoDatos()
        option = int(input("Seleccione una opción: "))

def GraficaDatos():
    print(Fore.CYAN + 'se están graficando datos')
    print(Fore.GREEN+'¿Desea salir de la grafica de datos?')
    print('1. Si')
    print('2. No')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))  
    if option == 1:
        menu()
    elif option == 2:
        GestionDatos()
    else:
        print("opcion invalida")
        print()
        GraficaDatos()
        option = int(input("Seleccione una opción: "))

def menu():
    print(Fore.YELLOW +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('|                    1. Cargar archivo              |')
    print('*                    2. Gestionar peliculas         *')
    print('|                    3. Filtrado                    |')
    print('*                    4. Grafica                     *')
    print('|                    5. Regresar                    |')
    print('*                    6. Salir                       *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    option = int(input(Fore.GREEN +"Seleccione una opción: "))  
    if option == 1:
        cargarArchivos()
    elif option == 2:
        GestionDatos()
    elif option == 3:
        FiltradoDatos()
    elif option == 4:
        GraficaDatos()
    elif option == 5:
        inicio()
    elif option == 6:
        print(Fore.WHITE+'adios')
        exit()
    else:
        print("opcion invalida")
        print()
        menu()
        option = int(input("Seleccione una opción: "))

def inicio():
    print(Fore.RED +'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('|                     Inicio                        *')
    print('*        Lenguajes formales de programación         |')
    print('|                   Sección B-                      *')
    print('*                Carné: 202109705                   |')
    print('|             Juan Pablo Samayoa Ruiz               *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('*                    1. Menu                        |')
    print('|                    2. Salir                       *')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

    option = int(input(Fore.GREEN +"Seleccione una opción: "))  
    if option == 1:
        menu()
    elif option == 2:
        print(Fore.WHITE+'adios')
        Exit()
    else:
        print("opcion invalida")
        print()
        inicio()
        option = int(input("Seleccione una opción: "))
inicio()