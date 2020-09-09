def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if (arr[i] < arr[j]):
                arr[j], arr[i] = arr[i], arr[j]
    return arr


lista = [7, 6, 4, 9, 8, 2, 3, 0, 10, 1, 5]
print(lista, "não ordenada")

lista = bubbleSort(lista)
print(lista, "lista ordenada")