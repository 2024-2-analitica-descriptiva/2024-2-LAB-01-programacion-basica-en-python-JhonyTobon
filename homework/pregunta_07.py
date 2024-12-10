"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    from itertools import groupby
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
    list_number_key = []
    for key, group in grouped:
        letras = [letra for letra, value in group]
        list_number_key.append((int(key), letras))
    
    return list_number_key



"""
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
