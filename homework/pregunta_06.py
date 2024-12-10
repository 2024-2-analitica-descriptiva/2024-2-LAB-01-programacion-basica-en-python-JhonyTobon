"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Separar la data para operar
    key_value = [line[-1] for line in clean_list]
    key_value = [z.replace(',','\t')for z in key_value]
    key_value = [z.split('\t')for z in key_value]
    # Diccionario para almacenar el mínimo y máximo de cada clave
    min_max_values = {}

    # Procesamos los datos
    for row in key_value:
        for item in row:
            # Dividimos cada elemento por ':'
            key, value = item.split(':')
            value = int(value)  # Convertimos el valor a entero
        
            # Si la clave no existe, crear el mínimo y máximo
            if key not in min_max_values:
                min_max_values[key] = [value, value]
            else:
            # Actualizar el valor mínimo y máximo
                min_max_values[key][0] = min(min_max_values[key][0], value)  # Valor mínimo
                min_max_values[key][1] = max(min_max_values[key][1], value)  # Valor máximo

        # Convertir el diccionario a una lista de tuplas ordenada por clave
        result = [(key, min_max_values[key][0], min_max_values[key][1]) for key in sorted(min_max_values.keys())]

    # Retornar la función
    return result
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
