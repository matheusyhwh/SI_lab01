def maximo(array):
    maior = array[0]
    for element in array:
        if element > maior:
            maior = element
    return maior
