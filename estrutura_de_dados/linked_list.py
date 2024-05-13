class Cell():

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():

    def __init__(self, root):
        self.root = root

    def insert(self, data):

        cell = self.root
        
        while cell.next:
            cell = cell.next
        cell.next = Cell(data)
    
    def remove(self, data):

        if self.root.data == data:
            self.root = self.root.next
        else:

            cell = self.root

            while cell.next and cell.next.data != data:
                cell = cell.next

            if not cell.next: cell.next = cell.next.next    

    def __str__(self):

        string = ''

        r = self.root

        while r != None:
            string += f'{r.data} '
            r = r.next
    
        return string

if __name__ == '__main__':
    linked = LinkedList(Cell('Vinicius'))
    linked.insert('Teste')
    linked.insert('Felix')
    linked.remove('Felix')
    linked.remove('Felix')
    print(linked.__str__())