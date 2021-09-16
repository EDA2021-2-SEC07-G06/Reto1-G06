﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from App.controller import initCatalogArrayList, initCatalogSingleLinked
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposicion en el museo")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog_type=int(input("Presiona 1 para cargar la lista con tipo Linked List y 2 para cargar la lista con tipo Array List."))
        if catalog_type==1:
            catalog = controller.initCatalogSingleLinked()
        elif catalog_type==2:
            catalog = controller.initCatalogArrayList()
        controller.loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['Artists'])))
        print('obras cargadas: ' + str(lt.size(catalog['Artworks'])))
    elif int(inputs[0]) == 2:
        sorttype=int(input('Para ordenamiento por insertionsort ingrese 1, por shellsort ingrese 2, por quicksort ingrese 3 y por mergesort ingrese 4'))
        cmpfunction=controller.callcmp
        if sorttype==1:
            ordlist=controller.sortlistinsertion(catalog, cmpfunction)
        elif sorttype==2:
            ordlist=controller.sortlistshell(catalog, cmpfunction)
        elif sorttype==3:
            ordlist=controller.sortlistquick(catalog, cmpfunction)
        elif sorttype==4:
            ordlist=controller.sortlistmerge(catalog, cmpfunction)
        size=int(input('ingrese el tamaño de la muestra que desea'))
        subordlist=controller.loadsublist(ordlist,0,size)
        print(subordlist)
    else:
        sys.exit(0)