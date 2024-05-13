
class Queque():

    def __init__(self):
        self.data = []
        self.total_elements = 0
    
    def enqueque(self, element):
        self.data = [element] + self.data
        self.total_elements += 1
    
    def dequeque(self):
        
        if self.total_elements > 0:
            self.data[self.total_elements-1]
            self.total_elements -= 1

    def __str__(self):
        string = ''


        for i in range(0, self.total_elements):
            string += f'{self.data[i]} '
        return string

if __name__ == '__main__':
    queque = Queque()
    queque.enqueque(1)
    queque.enqueque(2)
    queque.enqueque(3)
    queque.enqueque(4)
    queque.enqueque(5)
    queque.dequeque()
    queque.dequeque()
    queque.dequeque()
    queque.enqueque(44)
    print(queque.__str__())