"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Separar la data para operar
    coder = [(line[-1]) for line in clean_list]
    coder = [z.split (',') for z in coder]
    #Crear un diccionario vacío
    key_counter = {}
    #Iterar sobre los datos, dividir el ":", alojar cada clave y acumular las veces que aparece
    for key_value in coder:
        for item in key_value:
            key, value = item.split(':')
            if key in key_counter:
                key_counter[key] += 1
            else:
                key_counter[key] = 1

    #Ordenar el diccionario alfabéticamente por la clave
    ordered_key_counter = {k: key_counter[k] for k in sorted(key_counter)}


    return ordered_key_counter
    
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
