lista = [0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82]

def swap(i , j):
    tmp      = lista[j]
    lista[j] = lista[i]
    lista[i] = tmp

def selection():

    for i in range(0, len(lista)):

        pos = i

        for j in range((i+1), len(lista)):

            if lista[j] > lista[pos]:
                pos = j
        
        swap(pos, i)


if __name__ == '__main__':
    selection()
    print(lista)