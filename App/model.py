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


from DISClib.DataStructures.arraylist import addFirst
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
def cmpdaterange(artwork,start,end):
    return datetime.strptime(artwork['DateAcquired'],'%Y-%m-%d')>start and datetime.strptime(artwork['DateAcquired'],'%Y-%m-%d')<end
def daterangelist(lst,cmp,start,end):
    size=lt.size(lst)
    newlist=lt.newList('ARRAY_LIST', cmpfunction=None)
    for i in range(0,size):
        artwork=lt.getElement(lst,i)
        if cmp(artwork,start,end):
            lt.addFirst(newlist,artwork)
    return newlist
def cleanordlist(catalog):
    newlist=lt.newList('ARRAY_LIST',cmpfunction=None)
    for i in range(0,lt.size(catalog)):
        if catalog['elements'][i]['dateAcquired']!=(''):
            lt.addFirst(newlist,catalog[i])
    return newlist

def insertionsort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpfunction(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst
def mergesort(lst, cmpfunction):
    size = lt.size(lst)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lst, 1, mid)
        rightlist = lt.subList(lst, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        mergesort(leftlist, cmpfunction)
        mergesort(rightlist, cmpfunction)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpfunction(elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(lst, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lt.changeInfo(lst, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lst, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lst, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return lst
def partition(lst, lo, hi, cmpfunction):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if cmpfunction(
           lt.getElement(lst, leader), lt.getElement(lst, hi)):
            lt.exchange(lst, follower, leader)
            follower += 1
        leader += 1
    lt.exchange(lst, follower, hi)
    return follower


def quicksort(lst, lo, hi, cmpfunction):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lst, lo, hi, cmpfunction)
    quicksort(lst, lo, pivot-1, cmpfunction)
    quicksort(lst, pivot+1, hi, cmpfunction)


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
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento