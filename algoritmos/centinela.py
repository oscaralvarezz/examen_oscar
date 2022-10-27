def centinela(lista, buscado):
    "Método de busqueda (secuencial)"
    posicion = -1
    i = 0
    while( i < len(lista)) and (posicion = -1):
        if (lista[i]= buscado):
            posicion = i
        i += 1
    return posicion
