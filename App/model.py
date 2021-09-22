"""
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
def newCatalog():
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
    for i in range(0,lt.size(catalog)):
        if catalog['elements'][i]['DateAcquired']!=(''):
            lt.addLast(newlist,catalog['elements'][i])
    return newlist
def artistsearchbyID(ID, generalcatalog):
    Name=''
    for i in range (lt.size(generalcatalog['Artists'])):
        if str(ID) == str(generalcatalog['Artists']['elements'][i]['ConstituentID']):
            print(str(ID) == str(generalcatalog['Artists']['elements'][i]['ConstituentID']))
            Name= str(generalcatalog['Artists']['elements'][i]['DisplayName'])
            break
        else:
            Name= 'Not Found'
    return Name
def adjustvalues(resultcatalog, headers,generalcatalog):
    size=len(headers)
    sizecatalog=lt.size(resultcatalog)
    mainlist=[]
    secondarylist=[]
    IDlist=[]
    Artistcount=0
    purchases=0
    for item in range(0,sizecatalog):
        ID=str(resultcatalog['elements'][item]['ConstituentID'])
        secondarylist.append(str(artistsearchbyID(ID,generalcatalog)))
        if ID not in IDlist:
            Artistcount += 1
        IDlist.append(ID)
        if resultcatalog['elements'][item]['CreditLine']=='Purchase':
            purchases+=1
        for i in range (1,size):
            secondarylist.append(resultcatalog['elements'][item][headers[i]])
        mainlist.append(secondarylist)
        secondarylist=[]
    return mainlist, Artistcount,purchases
#req 1
def cmpartistrange(artist,start,end):
    return datetime.strptime(artist['BeginDate'],'%Y') >= start and datetime.strptime(artist['BeginDate'],'%Y')<=end
def adjustartistvalues(resultcatalog, headers):
    size=len(headers)
    sizecatalog=lt.size(resultcatalog)
    mainlist=[]
    secondarylist=[]
    IDlist=[]
    Artistcount=0
    for item in range(0,sizecatalog):
        ID=str(resultcatalog['elements'][item]['ConstituentID'])
        if ID not in IDlist:
            Artistcount += 1
        IDlist.append(ID)
        for i in range (0,size):
            secondarylist.append(resultcatalog['elements'][item][headers[i]])
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
    for i in range(0,lt.size(catalog)):
        if catalog['elements'][i]['BeginDate']!=('0'):
            lt.addLast(newlist,catalog['elements'][i])
    return newlist
#req4
def dictionarymaker(artists, artworks):
    copia=artworks
    dictionary={}
    Nationalities=[]
    headers=['Title','DateAcquired','Medium','Dimensions']
    for i in lt.iterator(artists):
        if (i['Nationality'] not in dictionary.keys()) and i['Nationality'] != (''):
            dictionary[i['Nationality']]=lt.newList('ARRAY_LIST',cmpfunction=0)
            Nationalities.append(i['Nationality'])
    for Artwork in lt.iterator(artworks):
        characteristics=lt.newList('ARRAY_LIST',cmpfunction=0)
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


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento