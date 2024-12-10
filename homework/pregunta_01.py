"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    lista_lineas = open("files/input/data.csv", "r").readlines()
    lista_sin_salto = [line.replace("\n","") for line in lista_lineas]
    lista_de_listas = [str.split("\t") for str in lista_sin_salto]
    lista_de_listas = sum(int(lista_de_listas[1]) for lista_de_listas in lista_de_listas)
    return lista_de_listas

"""
    Retorne la suma de la segunda columna
    Rta/
    214

    """
