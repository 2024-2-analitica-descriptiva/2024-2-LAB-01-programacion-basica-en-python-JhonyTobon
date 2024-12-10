"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy."""



def pregunta_02():
    from collections import Counter
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Seleccionar solo la data relevante
    column_01 = [line[0] for line in clean_list]
    #Convertir en lista y ordenar alfabéticamente
    
    return sorted(list(Counter(column_01).items()))


"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
