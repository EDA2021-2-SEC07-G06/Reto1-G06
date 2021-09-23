﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from collections import OrderedDict
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime
from DISClib.Utils import error as error
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalogSingleLinked():
    catalog = {'Artists': None,
               'Artworks': None,
               }

    catalog['Artists'] = lt.newList('ARRAY_LIST', cmpfunction=None)
    catalog['Artworks'] = lt.newList('ARRAY_LIST', cmpfunction=None)

    return catalog

def newCatalogArrayList():
    catalog = {'Artists': None,
               'Artworks': None,
               }

    catalog['Artists'] = lt.newList('ARRAY_LIST', cmpfunction=None)
    catalog['Artworks'] = lt.newList('ARRAY_LIST', cmpfunction=None)

    return catalog
# Funciones para agregar informacion al catalogo
def addArtist(catalog, Artist):
    lt.addLast(catalog['Artists'], Artist)
def addArtwork(catalog, Artwork):
    lt.addLast(catalog['Artworks'], Artwork)
def cmpArtworkByDateAcquired(artwork1,artwork2):
    if artwork1['DateAcquired']!=str('') and artwork2['DateAcquired'] !=str(''):
        condition=(datetime.strptime(artwork1['DateAcquired'],'%Y-%m-%d')< datetime.strptime(artwork2['DateAcquired'],'%Y-%m-%d'))
    else:
        condition=False
    return condition
def subList(lst, pos, numelem):
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')
def cmpartworkrange(artwork,start,end):
    return datetime.strptime(artwork['DateAcquired'],'%Y-%m-%d')>=start and datetime.strptime(artwork['DateAcquired'],'%Y-%m-%d')<=end
def daterangelist(lst,cmp,start,end):
    size=lt.size(lst)
    newlist=lt.newList('ARRAY_LIST', cmpfunction=None)
    for i in range(0,size):
        artist=lt.getElement(lst,i)
        if cmp(artist,start,end):
            lt.addLast(newlist,artist)
    return newlist
def cleanartworksordlist(catalog):
    newlist=lt.newList('ARRAY_LIST',cmpfunction=None)
    for item in lt.iterator(catalog):
        if item['DateAcquired']!=(''):
            lt.addLast(newlist,item)
    return newlist
def artistsearchbyID(ID, generalcatalog):
    Name=''
    for artist in lt.iterator(generalcatalog['Artists']):
        if str(ID) == str(artist['ConstituentID']):
            Name= str(artist['DisplayName'])
            break
        else:
            Name= 'Not Found'
    return Name
def adjustvalues(resultcatalog, headers,generalcatalog):
    mainlist=[]
    secondarylist=[]
    IDlist=[]
    Artistcount=0
    purchases=0
    for item in lt.iterator(resultcatalog):
        ID=str(item['ConstituentID']).replace('[','').replace(']','')
        secondarylist.append(str(artistsearchbyID(ID,generalcatalog)))
        print(ID)
        if ID not in IDlist:
            Artistcount += 1
        IDlist.append(ID)
        if item['CreditLine']=='Purchase':
            purchases+=1
        for elemento in range(1,len(headers)):
            secondarylist.append(item[headers[elemento]])
        mainlist.append(secondarylist)
        secondarylist=[]
    return mainlist, Artistcount,purchases
#req 1
def cmpartistrange(artist,start,end):
    return datetime.strptime(artist['BeginDate'],'%Y') >= start and datetime.strptime(artist['BeginDate'],'%Y')<=end
def adjustartistvalues(resultcatalog, headers):
    mainlist=[]
    secondarylist=[]
    IDlist=[]
    Artistcount=0
    for item in lt.iterator(resultcatalog):
        ID=str(item['ConstituentID'])
        if ID not in IDlist:
            Artistcount += 1
        IDlist.append(ID)
        for elemento in headers:
            secondarylist.append(item[elemento])
        mainlist.append(secondarylist)
        secondarylist=[]
    return mainlist, Artistcount
def cmpArtistByDateAcquired(artist1,artist2):
    if artist1['BeginDate'] !=str('0') and artist2['BeginDate'] !=str('0'):
        condition= int(artist1['BeginDate']) < int(artist2['BeginDate'])
    else:
        condition=False
    return condition    
def cleanartistordlist(catalog):
    newlist=lt.newList('ARRAY_LIST',cmpfunction=None)
    for i in lt.iterator(catalog):
        if i['BeginDate']!=('0'):
            lt.addLast(newlist,i)
    return newlist
#req4
def dictionarymaker(artists, artworks):
    dictionary={}
    Nationalities=[]
    for i in lt.iterator(artists):
        if (i['Nationality'] not in dictionary.keys()) and i['Nationality'] != (''):
            dictionary[i['Nationality']]=lt.newList('ARRAY_LIST',cmpfunction=0)
            Nationalities.append(i['Nationality'])
    for Artwork in lt.iterator(artworks):
        for Artist in lt.iterator(artists):
            if (Artist['ConstituentID']==str(Artwork['ConstituentID']).replace('[','').replace(']','') and Artist['Nationality']!=''):
                lt.addLast(dictionary[Artist['Nationality']],Artwork)
    return dictionary,Nationalities
def ArtByNation(dictionary,Nationalities):
    newlist=lt.newList('ARRAY_LIST', cmpfunction=0)
    for Nation in Nationalities:
        dict=OrderedDict()
        dict['Country']=Nation
        dict['size']=lt.size(dictionary[Nation])
        lt.addLast(newlist,dict)
    return newlist
def nationcmp(nation1,nation2):
    return nation1['size']>nation2['size']
def greatestlist(headers,dictionary,greatest,generalcatalog):
    newlist=lt.newList('ARRAY_LIST', cmpfunction=0)
    for i in lt.iterator(dictionary[greatest]):
        dict=OrderedDict()
        ID= i['ConstituentID'].replace('[','').replace(']','')
        name=artistsearchbyID(ID, generalcatalog)
        dict['Artist']=name
        dict['Title']=i['Title']
        dict['DateAcquired']=i['DateAcquired']
        dict['Medium']=i['Medium']
        dict['Dimensions']=i['Dimensions']
        lt.addLast(newlist,dict)
    return newlist


def sort(lst, cmpfunction):
    quicksort(lst, 1, lt.size(lst), cmpfunction)
    return lst
def shellsort(lst, cmpfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpfunction(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst

def clasificar_obras_artista_por_tecnica(artists, artworks, nombre):
    totalobras=0
    IDartista=""
    medios=[]
    for artist in artists:
        if artist[1] == nombre:
            IDartista=artist[0]
    
    for artwork in artworks:
        if artwork[2]==IDartista:
            totalobras+=1
            medionuevo=True
            for k in medios:
                if artwork[4]==medios[k]:
                    medionuevo=False
                    posiciondemedio=k
            if medionuevo==True:
                medioconfrecuencia=[artwork[4],1]
                medios.append(medioconfrecuencia)
            else:
                medios[posiciondemedio][1]+=1

    mediomasfrecuente=[""]
    frecuenciamediomasfrecuente=0
    obras_tecnica_mas_usada=[]
    for l in medios:
        if medios[l][1]>frecuenciamediomasfrecuente:
            frecuenciamediomasfrecuente=medios[l][0]
            mediomasfrecuente=medios[l][1]

    for artwork in artworks:
        if artwork[2]==IDartista and artwork[5]==mediomasfrecuente:
            Titulo=artwork[1]
            Fecha=artwork[3]
            Medio=artwork[4]
            Dimensiones=artwork[5]
            obra=[Titulo, Fecha, Medio, Dimensiones]
            obras_tecnica_mas_usada.append(obra)
    
    totalnumerodemedios=int(len(medios))
    return totalobras, totalnumerodemedios, mediomasfrecuente, obras_tecnica_mas_usada

    
def transferatworks(artworks, department):
    totalobrasatransferir=0
    costototal=0
    totalweight=0
    lista_mas_costosos=[]
    lista_mas_antiguos=[]

    for artwork in artworks:
        if artwork[9]==department:
            totalobrasatransferir+=1
            metroscuadrados=0
            metroscubicos=0
            costopormetrocuadrado=0
            costopormetrocubico=0
            Weight=0
            costoporpeso=0
            if  artwork[19] != None and artwork[17] != None:
                length=float(artwork[17])
                width=float(artwork[19])
                metroscuadrados=(length*width)/(10**2)
                costopormetrocuadrado=(72*metroscuadrados)
                if artwork[15] != None:
                    height=float(artwork[15])
                    metroscubicos=(length*width*height)/(10**3)
                    costopormetrocubico=72*metroscubicos
            if artwork[18] != None:
                Weight=float(artwork[18])
                costoporpeso=72*Weight
            if costopormetrocuadrado == 0 and costopormetrocubico == 0 and costoporpeso == 0:
                costoobra=48
            else:
                costoobra=max(costopormetrocuadrado, costopormetrocubico, costoporpeso)
            costototal+=costoobra
            totalweight+=Weight

            for j in range(0,5):
                if lista_mas_antiguos[j] == None or datetime.strptime(artwork["Date"], '%Y') < datetime.strptime(lista_mas_antiguos[j][4],'%Y'): #Usando comparacion fechas
                    if j < 4:
                        lista_mas_antiguos[j+1]=lista_mas_antiguos[j]
                    lista_mas_antiguos[j]=[artwork[0],artwork[1],artwork[4],artwork[3],artwork[5],artwork[8],costoobra, artwork[12]]
                if lista_mas_costosos[j] == None or costoobra > lista_mas_costosos[j][7]: 
                    if j < 4:
                        lista_mas_costosos[j+1]=lista_mas_costosos[j]
                    lista_mas_costosos[j]=lista_mas_antiguos[j]=[artwork[0],artwork[1],artwork[4],artwork[3],artwork[5],artwork[8],costoobra, artwork[12]]

    return totalobrasatransferir, costototal, totalweight, lista_mas_antiguos, lista_mas_costosos
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento