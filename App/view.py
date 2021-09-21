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

import prettytable
from tabulate import tabulate
import config as cf
import sys
from datetime import datetime
import controller
from DISClib.ADT import list as lt
from prettytable import PrettyTable
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
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['Artists'])))
        print('Obras Cargadas: ' + str(lt.size(catalog['Artworks'])))
    elif int(inputs[0]) == 2:
        artistslist=catalog['Artists']
        sortcmp=controller.callartistcmp
        ordlist=controller.sortlistinsertion(artistslist,sortcmp)
        size=lt.size(ordlist)
        startdate=str(input('Ingrese la fecha inicial '))
        startdate=datetime.strptime(startdate,'%Y-%m-%d')
        enddate=str(input('Ingrese la fecha final '))
        enddate=datetime.strptime(enddate,'%Y-%m-%d')
        cmpfunction=controller.callartistrangecmp
        rangelist=controller.callartistrangelist(ordlist,cmpfunction,startdate,enddate)
        header=['DisplayName','BeginDate','EndDate','Nationality','Gender']
        adjustvalues,Artistcount=controller.calladjustvalues(rangelist, header, catalog)
        finallist= adjustvalues[0:3] + adjustvalues[len(adjustvalues)-3:len(adjustvalues)]
        maintable=PrettyTable()
        maintable.field_names = ['DisplayName','BeginDate','EndDate','Nationality','Gender']
        maintable.align='l'
        maintable._max_width= {'DisplayName':20,'BeginDate':10,'EndDate':10,'Nationality':15,'Gender':10}
        for i in range(0,len(finallist)):
            maintable.add_row(finallist[i])
        print(maintable)
    elif int(inputs[0]) == 3:
        artworkslist=catalog['Artworks']
        sortcmp=controller.callcmp
        ordlist=controller.sortlistinsertion(artworkslist,sortcmp)
        size=lt.size(ordlist)
        startdate=str(input('Ingrese la fecha inicial '))
        startdate=datetime.strptime(startdate,'%Y-%m-%d')
        enddate=str(input('Ingrese la fecha final '))
        enddate=datetime.strptime(enddate,'%Y-%m-%d')
        cmpfunction=controller.callartworkrangecmp
        rangelist=controller.callartworkrangelist(ordlist,cmpfunction,startdate,enddate)
        header=['Artists','Title','DateAcquired','Medium','Dimensions']
        adjustvalues,Artistcount,purchases=controller.calladjustvalues(rangelist, header, catalog)
        finallist= adjustvalues[0:3] + adjustvalues[len(adjustvalues)-3:len(adjustvalues)]
        maintable=PrettyTable()
        maintable.field_names = ['Artists','Title','DateAcquired','Medium','Dimensions']
        maintable.align='l'
        maintable._max_width= {'Artists':12,'Title':30,'DateAcquired':10,'Medium':20,'Dimensions':30}
        for i in range(0,len(finallist)):
            maintable.add_row(finallist[i])
        print('The MOMA acquired '+ str(len(adjustvalues)) +' unique pieces between '+ str(startdate) +' and '+ str(enddate)+'\n'+'With '+ str(Artistcount)+' different artists and purchased '+ str(purchases) + ' of them \n')
        print('the first and last 3 artworks in the range are: \n')
        print(maintable)
    else:
        sys.exit(0)