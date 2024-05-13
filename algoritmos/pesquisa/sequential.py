lista = [0,1,5,3,15,16,9,10,4,3,30,5,20,48,71,82]

def sequential(val):

    for element in lista:
        if element == val: return True
    return False

if __name__ == '__main__':

    print('FOUND') if sequential(-1) else  print('NOT FOUND')
    print('FOUND') if sequential(4)  else  print('NOT FOUND')
    print('FOUND') if sequential(0)  else  print('NOT FOUND')
    print('FOUND') if sequential(82) else  print('NOT FOUND')
    print('FOUND') if sequential(88) else  print('NOT FOUND')