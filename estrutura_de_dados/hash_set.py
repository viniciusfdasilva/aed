
class HashSet():

    def __init__(self, type):
        self.type = type
        self.hash = []

    def insert(self, data):

        if type(data) == self.type and not self.__contains(data):
            self.hash.append(data)

    def remove(self, data):
        self.hash.remove(data)

    def __contains(self, data):
        return data in self.hash

    def __str__(self):
        string = ''

        for element in self.hash:
            string += f'{element} '
        return string

if __name__ == '__main__':
    
    hashset = HashSet(str)
    hashset.insert('Vinicius')
    hashset.insert(1)
    hashset.insert(4)
    hashset.insert('Teste')
    print(hashset.__str__())
    hashset.remove('Vinicius')
    print(hashset.__str__())