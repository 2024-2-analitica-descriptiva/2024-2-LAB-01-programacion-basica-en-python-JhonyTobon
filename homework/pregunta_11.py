"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Crear una lista vacía para ir pegando los datos
    dict_letter_sum={}
    #Recorrer la data para traer los datos y su formato
    for line in clean_list:
            columna_04 = line[3].split(',')
            columna_02 = int(line[1])
    #Armar el diccionario con cada letra de la col4 e ir sumando la col2
            for letter in columna_04:
                    if letter not in dict_letter_sum:
                        dict_letter_sum[letter] = columna_02
                    else:
                        dict_letter_sum[letter] += columna_02

    #traer el diccionario ordenado
    dict_letter_sum = dict(sorted(dict_letter_sum.items()))

    return dict_letter_sum 
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
