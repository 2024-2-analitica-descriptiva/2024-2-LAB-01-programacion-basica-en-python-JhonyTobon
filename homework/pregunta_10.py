"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Crear una lista vacía para ir pegando los datos
    list_code_counter=[]
    #Recorrer la data para traer los datos
    for line in clean_list:
        columna_01 = line[0]
        columna_04 = line[3].split(',')
        columna_05 = line[4].split(',')
    #Contar los datos de las columnas 4 y 5
        contar_col04 = len(columna_04)
        contar_col05 = len(columna_05)
    #pegar los datos según la orden, letra de la col 1, cuenta de la col 4 y 5
        list_code_counter.append((columna_01, contar_col04, contar_col05))

    return list_code_counter 
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
