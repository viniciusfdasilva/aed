lista = sorted([0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82])

def binary_callable(val):
    return binary(val, 0, len(lista)-1)

def binary(val, i, j):
    
    middle = int((i + j)/2)

    if j < i:
        return False 
    elif val == lista[middle]:
        return True
    elif val > lista[middle]:
        return binary(val, middle+1, j)
    else:
        return binary(val, i, middle-1)

if __name__ == '__main__':
    print('FOUND') if binary_callable(-1) else  print('NOT FOUND')
    print('FOUND') if binary_callable(4)  else  print('NOT FOUND')
    print('FOUND') if binary_callable(0)  else  print('NOT FOUND')
    print('FOUND') if binary_callable(82) else  print('NOT FOUND')
    print('FOUND') if binary_callable(88) else  print('NOT FOUND')