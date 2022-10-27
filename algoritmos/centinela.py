def centinela(lista, buscado):
    "Método de busqueda (secuencial)"
    posicion = -1
    for i in range(0,len(lista)):
        if (lista[i]== buscado):
            posicion = i
            break
    return posicion

lista = (1,4,6,3,7)
print(centinela(lista,6))
