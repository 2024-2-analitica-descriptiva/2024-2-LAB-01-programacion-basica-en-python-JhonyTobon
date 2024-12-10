"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_08():

    #Leer y limpiar la data
    open_data = open('files/input/data.csv','r').readlines()
    open_data = [z.replace('\n','')for z in open_data]
    clean_list = [z.split('\t')for z in open_data]
    #Separar la data para operar
    data_list = [(line[0],line[1]) for line in clean_list]
    #Organizar las tuplas por la columna 1
    data_sorted = sorted(data_list, key=lambda x: x[1])
    #Agrupar, crear la lista y retornar la pregunta 07
    grouped = groupby(data_sorted, key=lambda x: x[1])
    list_independent = []
    for key, group in grouped:
    # Usamos un set para evitar duplicados
        letras = set(letra for letra, value in group)
    #Conversiones a enter y a lista ordenada
        list_independent.append((int(key), sorted(list(letras))))
    
    return list_independent
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
