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
 """

import config as cf
import model
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import insertionsort as insrt
from DISClib.Algorithms.Sorting import shellsort as shllsrt
from DISClib.Algorithms.Sorting import mergesort as mrg
from DISClib.ADT import list as lt
from datetime import datetime
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo del MOMA
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    Artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistsfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)

def loadArtworks(catalog):
    Artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(Artworksfile, encoding='utf-8'))
    for Artwork in input_file:
        model.addArtwork(catalog, Artwork)
def loadsublist(lst,pos,numelem):
    return model.sublist(lst,pos,numelem)
#req1
def callartistrangelist(catalog,cmp,start,end):
    size=lt.size(catalog)
    for i in range(0,size ):
        condition1=start < (datetime.strptime(catalog['elements'][0]['BeginDate'],'%Y-%m-%d' ))
        condition2=end > datetime.strptime(catalog['elements'][size-1]['BeginDate'],'%Y-%m-%d' )
        if condition1 and condition2:
            result=print('Invalid Range')
        elif (not condition1) and (not condition2):
            result=model.daterangelist(catalog,cmp,start,end)
        return result
def callartistrangecmp(artist,start,end):
    if start != ('') and end != ('') and artist['BeginDate'] != (''):
        var= model.cmpartistrange(artist,start,end)
    else:
        var=False
    return var
def calladjustartistvalues(catalog,headers,secondarycatalog):
    return model.adjustartistvalues(catalog,headers,secondarycatalog)
def callartistcmp(artist1,artist2):
    return model.cmpArtistByDateAcquired(artist1,artist2)
#req2
def callcmp(artwork1,artwork2):
    return model.cmpArtworkByDateAcquired(artwork1,artwork2)
def callartworkrangecmp(artwork,start,end):
    if start != ('') and end != ('') and artwork['DateAcquired'] != (''):
        var= model.cmpartworkrange(artwork,start,end)
    else:
        var=False
    return var
def callartworkrangelist(catalog,cmp,start,end):
    size=lt.size(catalog)
    for i in range(0,size ):
        condition1=start < (datetime.strptime(catalog['elements'][0]['DateAcquired'],'%Y-%m-%d' ))
        condition2=end > datetime.strptime(catalog['elements'][size-1]['DateAcquired'],'%Y-%m-%d' )
        if condition1 and condition2:
            result=print('Invalid Range')
        elif (not condition1) and (not condition2):
            result=model.daterangelist(catalog,cmp,start,end)
    return result
def cleanordlist(catalog):
    return model.cleanordlist(catalog)
def calladjustvalues(catalog,headers,secondarycatalog):
    return model.adjustvalues(catalog,headers,secondarycatalog)
def callshowlist(lst):
    return 
def sortlistinsertion(catalog,cmpfunction):
    return insrt.sort(catalog,cmpfunction)
def sortlistshell(catalog,cmpfunction):
    return shllsrt.sort(catalog,cmpfunction)
def sortlistquick(catalog,cmpfunction):
    return qck.sort(catalog,cmpfunction)
def sortlistmerge(catalog,cmpfunction):
    return mrg.sort(catalog,cmpfunction)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
