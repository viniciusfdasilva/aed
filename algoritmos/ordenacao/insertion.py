
lista = [0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82]

def swap(i, j):
    tmp = lista[i]
    lista[i] = lista[j]
    lista[j] = tmp

def insertion():

    for i in range(0, len(lista)):
        j = i
        
        while j > 0 and lista[j-1] > lista[j]:
            swap(j, j-1)
            j -= 1

if __name__ == '__main__':
    insertion()
    print(lista)