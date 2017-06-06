def maximo(array):
    maior = array[0]
    for element in array:
        if element > maior:
            maior = element
    return maior

def minimo(array):
    menor = array[0]
    for element in array:
        if element < menor:
            menor = element
    return menor
