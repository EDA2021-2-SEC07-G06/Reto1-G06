"""
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

import config as cf
import sys
from datetime import datetime
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
        artworklist=catalog['Artworks']
        sorttype=int(input('Para ordenamiento por insertionsort ingrese 1, por shellsort ingrese 2, por quicksort ingrese 3 y por mergesort ingrese 4'))
        cmpfunction=controller.callcmp
        if sorttype==1:
            ordlist=controller.sortlistinsertion(artworklist, cmpfunction)
        elif sorttype==2:
            ordlist=controller.sortlistshell(artworklist, cmpfunction)
        elif sorttype==3:
            ordlist=controller.sortlistquick(artworklist, cmpfunction)
        elif sorttype==4:
            ordlist=controller.sortlistmerge(artworklist, cmpfunction)
        order=int(input('ingrese el tamaño de la muestra que desea'))
        subordlist=controller.loadsublist(ordlist,0,order)
        print(subordlist)
    
    elif int(inputs[0])==4:
        nombre=input("Escribe el nombre del artista: \n")
        artworks=catalog["Artworks"]
        artists=catalog["Artists"]
        resultados_funcion_opcion4=controller.clasificarobrasartista(artists, artworks, nombre)
        Totalobras=resultados_funcion_opcion4[0]
        Totaltecnicas=resultados_funcion_opcion4[1]
        Tecnicamasutilizada=resultados_funcion_opcion4[2]
        Lista_obras_con_tecnica=resultados_funcion_opcion4[3]

        print(nombre + " has " + str(Totalobras) + " pieces in his/her name \n" +
        "There are " +str(Totaltecnicas) + " different mediums/techniques in his/her work \n" +
        "His/her most used technique is "+Tecnicamasutilizada[0] +"\n")
        "The items in his/her collection using "+Tecnicamasutilizada[0]+" are: \n"
        for i in Lista_obras_con_tecnica:
            print(Lista_obras_con_tecnica[i]+"\n")

    elif int(inputs[0] == 6):
        departamento=input("Escoge el departamento del cual quiere transferir las obras.")
        artworklist=catalog["Artworks"]
        resultados=controller.transferartworks(artworklist, departamento)
        listamascostosos=resultados[4]
        listamasantiguos=resultados[3]
        print("The MoMA is going to transport 394 artifacts from the Drawings & Prints \n" +
         "REMEMBER!, NOT all MoMAs data is complete!!! These are estimates. \n" +
        "Estimated cargo weight (kg) :" + str(resultados[2]) +"\n"+
        "Estimated cargo cost (USD) :" + str(resultados[1]) +"\n"+
        "The TOP 5 most expensive items to transport are:"
        + str(listamascostosos[0]) + "\n"
        + str(listamascostosos[1]) + "\n"
        + str(listamascostosos[2]) + "\n"
        + str(listamascostosos[3]) + "\n"
        + str(listamascostosos[4]) + "\n" +
        "The TOP 5 oldest items to transport are:"
        + str(listamasantiguos[0]) + "\n"
        + str(listamasantiguos[1]) + "\n"
        + str(listamasantiguos[2]) + "\n"
        + str(listamasantiguos[3]) + "\n"
        + str(listamasantiguos[4]))
        artworkslist=catalog['Artworks']
        sortcmp=controller.callcmp
        ordlist=controller.sortlistinsertion(artworkslist,sortcmp)
        cleanordlist=controller.cleanordlist(ordlist)
        size=lt.size(cleanordlist)
        startdate=str(input('Ingrese la fecha inicial '))
        startdate=datetime.strptime(startdate,'%Y-%m-%d')
        enddate=str(input('Ingrese la fecha final '))
        enddate=datetime.strptime(enddate,'%Y-%m-%d')
    elif int(inputs[0])==5:
        cmpfunction=controller.callartworkrangecmp
        rangelist=controller.callartworkrangelist(ordlist,cmpfunction,startdate,enddate)
        rangelist=controller.sortlistinsertion(rangelist,sortcmp)
        header=['Artists','Title','DateAcquired','Medium','Dimensions']
        adjustvalues,Artistcount,purchases=controller.calladjustvalues(rangelist, header, catalog)
        finallist= adjustvalues[0:3] + adjustvalues[len(adjustvalues)-3:len(adjustvalues)]
        maintable=PrettyTable()
        maintable.field_names = ['Artists','Title','DateAcquired','Medium','Dimensions']
        maintable.align='l'
        maintable._max_width= {'Artists':12,'Title':30,'DateAcquired':10,'Medium':20,'Dimensions':30}
        for i in range(0,len(finallist)):
            maintable.add_row(finallist[i])
        print('\n The MOMA acquired '+ str(len(adjustvalues)) +' unique pieces between '+ str(startdate) +' and '+ str(enddate)+'\n'+'With '+ str(Artistcount)+' different artists and purchased '+ str(purchases) + ' of them \n')
        print('the first and last 3 artworks in the range are: \n')
        print(maintable)
    elif int(inputs[0])==5:
        artworkslist=catalog['Artworks']
        cmpfunction=controller.callnationcmp
        artistlist=catalog['Artists']
        dictionary,Nationalities=controller.calldictionarymaker( artistlist,artworkslist)
        ArtbyNation=controller.callArtByNation(dictionary,Nationalities)
        ordlist=controller.sortlistinsertion(ArtbyNation, cmpfunction)
        Nationstable=PrettyTable()
        Nationstable.field_names = ['Nationality','ArtWorks']
        Nationstable.align='l'
        Nationstable._max_width= {'Nationality':20,'ArtWorks':8}
        for Country in lt.iterator(ordlist):
            Nationstable.add_row([str(Country['Country']),str(Country['size'])])
        print('The TOP 10 Countries in the MOMA are:\n')
        print(Nationstable)
        greatest=ordlist['elements'][0]['Country']
        greatesttable=PrettyTable()
        headers=['Title','DateAcquired','Medium','Dimensions']
        greatestlist=controller.callgreatestlist(headers,dictionary,greatest,catalog)
        greatesttable.field_names =['Artist','Title','DateAcquired','Medium','Dimensions']
        greatesttable._max_width= {'Artists':12,'Title':30,'DateAcquired':10,'Medium':20,'Dimensions':30}
        for i in lt.iterator(greatestlist):
            greatesttable.add_row([str(i['Artist']), str(i['Title']), str(i['DateAcquired']), str(i['Medium']), str(i['Dimensions'])])
        print('The TOP nationality in the museum is '+  str(greatest)+ ' with ' + str(lt.size(greatestlist)) + ' unique pieces.')
        print('The first and last 3 objects in the American artwork list are:')
        print(greatesttable.get_string(start=0, end=3))
        print(greatesttable.get_string(start=lt.size(greatestlist)-3, end=lt.size(greatestlist)))
        print('hola')
        
        for i in range(0,(lt.size(rangelist))):
            print(rangelist['elements'][i]['ObjectID'])
    else:
        sys.exit(0)
