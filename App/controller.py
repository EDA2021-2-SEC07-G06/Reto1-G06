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
def callcmp(artwork1,artwork2):
    return model.cmpArtworkByDateAcquired(artwork1,artwork2)
def calldaterangecmp(artwork,start,end):
    if start != ('') and end != ('') and artwork['DateAcquired'] != (''):
        var= model.cmpdaterange(artwork,start,end)
    else:
        var=False
    return var
def calldaterangelist(lst,cmp,start,end):
    for i in range(0, lt.size(catalog['Artworks'])):
        condition1=(datetime.strptime(start,'%Y-%m-%d' in catalog['Artworks']['elements'][i]['DateAcquired'] ))
        condition2=(datetime.strptime(end,'%Y-%m-%d' in catalog['Artworks']['elements'][i]['DateAcquired'] ))
        if  not condition1:
            result=print('Fecha inicial no valida')
    return model.daterangelist(lst,cmp,start,end)
def callshowlist(lst):
    return 
def sortlistinsertion(catalog,cmpfunction):
    model.insertionsort(catalog,cmpfunction)
def sortlistshell(catalog,cmpfunction):
    model.shellsort(catalog,cmpfunction)
def sortlistquick(catalog,cmpfunction):
    model.quicksort(catalog,cmpfunction)
def sortlistmerge(catalog,cmpfunction):
    model.mergesort(catalog,cmpfunction)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
