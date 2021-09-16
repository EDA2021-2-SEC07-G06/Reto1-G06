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
def initCatalogSingleLinked():
    catalog = model.newCatalogSingleLinked()
    return catalog

def initCatalogArrayList():
    catalog = model.newCatalogArrayList()
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

def sortlistinsertion(catalog,cmpfunction):
    return model.insertionsort(catalog,cmpfunction)
def sortlistshell(catalog,cmpfunction):
    return model.shellsort(catalog,cmpfunction)
def sortlistquick(catalog,cmpfunction):
    return model.quicksort(catalog,cmpfunction)
def sortlistmerge(catalog,cmpfunction):
    return model.mergesort(catalog,cmpfunction)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
