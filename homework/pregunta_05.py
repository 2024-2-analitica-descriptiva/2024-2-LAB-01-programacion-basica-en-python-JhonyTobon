"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    #Leer y limpiar la data
    open_data=open('files/input/data.csv','r').readlines()
    open_data=[z.replace('\n','')for z in open_data]
    clean_list= [z.split('\t')for z in open_data]
    #Separar la data para operar
    letter = [(line[0], int(line[1])) for line in clean_list]
    #Tener la lista de ítems independientes
    listletter = set([x[0] for x in letter])
    #Crear una lista de tuplas vacía
    result=[]
    #Recorrer los datos y para traer por cada ítem el valor máximo y mínimo correspondiente
    for i in listletter:
        tmp = list(filter(lambda x: x[0]==i, letter))
        result.append((i,max(tmp)[1], min(tmp)[1]))
    #Ordenar los resultados
    result.sort()
    return result


"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
