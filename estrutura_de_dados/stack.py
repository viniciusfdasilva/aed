
class Stack():

    def __init__(self):
        self.data = []
    
    def pop(self):

        if len(self.data) == 0:
            raise IndexError('Stack out of range')
        else:
            last_element = self.data[0]
            self.data.remove(last_element)
            return last_element
    
    def push(self, data):

        self.data = self.data + [data]


    def __str__(self):
        string = ''
        for element in self.data:
            string += f'{element} '
        return string

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push(44)
    print(stack.__str__())