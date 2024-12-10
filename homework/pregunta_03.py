"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
#Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
#Separar la data para operar
    letter = [(line[0], int(line[1])) for line in clean_list]
#Crear un diccionario vacío
    dictionary = {}
#Iterar sobre los datos y acumular las sumas
    for letra, numero in letter:
        if letra in dictionary:
            dictionary[letra] += numero
        else:
            dictionary[letra] = numero

#Convertir el diccionario en una lista de tuplas (letra, suma)
        result = list(dictionary.items())
    
#Ordenar la lista alfabéticamente por la letra
    sort_result = sorted(result, key=lambda x: x[0])
    
    return sort_result
    
"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
