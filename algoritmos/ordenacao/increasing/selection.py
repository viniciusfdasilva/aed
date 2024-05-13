lista = [0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82]

def swap(i, j):
    tmp      = lista[i]
    lista[i] = lista[j]
    lista[j] = tmp

def selection():

    for i in range(0, len(lista)):

        less_pos = i

        for j in range((i+1), len(lista)):
            
            if lista[j] < lista[less_pos]:
                less_pos = j
        
        if less_pos != i:
            swap(less_pos, i)

if __name__ == '__main__':
    selection()

    print(lista)