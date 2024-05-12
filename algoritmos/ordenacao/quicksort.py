

lista = [0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82]

def quicksort_callable():
    return quicksort(0, len(lista)-1)

def swap(i, j):
    tmp = lista[i]
    lista[i] = lista[j]
    lista[j] = tmp
    return lista

def quicksort(i, j):
    global lista

    left  = i
    right = j

    pivo = int((i + j)/2)

    while i <= j:

        while lista[i] < lista[pivo]:
            i += 1
        
        while lista[j] > lista[pivo]:
            j -= 1
        
        if i <= j:
            lista = swap(i, j)
            i += 1
            j -= 1

    if left < j:
        quicksort(left, j)

    if i < right:
        quicksort(i, right)

def main():
    quicksort_callable()
    print(lista)



if __name__ == '__main__':
    main()