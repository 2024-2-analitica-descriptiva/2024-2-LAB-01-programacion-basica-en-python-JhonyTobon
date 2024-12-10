"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Crear una lista vacía para ir pegando los datos
    dict_key_value_sum={}
    #Recorrer la data para traer los datos y su formato
    for line in clean_list:
            position_01 = line[0]
            position_05 = line[4]
    #Partir los datos y realizar la suma de los valores en int al final del string
            values = position_05.split(',')
            sum_values = sum(int(z.split(':')[1])for z in values)
    #Armar el diccionario con cada letra de la col4 e ir sumando la col2
            if position_01 not in dict_key_value_sum:
                dict_key_value_sum[position_01] = sum_values
            else:
                dict_key_value_sum[position_01] += sum_values

    #traer el diccionario ordenado
    dict_key_value_sum = dict(sorted(dict_key_value_sum.items()))

    return dict_key_value_sum
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
