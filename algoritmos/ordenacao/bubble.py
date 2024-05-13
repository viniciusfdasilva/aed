
lista = [0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82]

def swap(i ,j):
    tmp      = lista[i]
    lista[i] = lista[j]
    lista[j] = tmp

def buble():
    
    for i in range(0, len(lista)):

        j = len(lista)-1
        less_pos = j

        while i < j:
            if lista[j] < lista[less_pos]:
                less_pos = j
            j -= 1
        
        if lista[less_pos] < lista[i]:
            swap(i, less_pos)


if __name__ == '__main__':
    buble()
    print(lista)