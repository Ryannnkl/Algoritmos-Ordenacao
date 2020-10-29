def selectionsort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
    return array

lista = [5,2,0,8,7,6,9,70,1,3,4]

print("lista não ordenada:",lista)

lista = sort(lista)
print("lista ordenada:",lista)