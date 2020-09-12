def particao(lista, inicio, fim):
    i = inicio
    pivot = lista[fim]

    for j in range(inicio, fim):

        if lista[j] <= pivot:

            lista[i], lista[j] = lista[j], lista[i]
            i = i + 1

    lista[i], lista[fim] = lista[fim], lista[i]
    return i


def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        pivot = particao(lista, inicio, fim)
        quickSort(lista, inicio, pivot - 1)
        quickSort(lista, pivot + 1, fim)


arr = [4, 10, 7, 3, 8, 9, 1, 5, 0, 2, 6]
n = len(arr)
print(arr, " lista não ordenada")
quickSort(arr)
print(arr, " lista ordenada")
