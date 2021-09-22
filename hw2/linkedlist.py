class Element:

    def __init__(self, element = None) -> None:
        self.next = None
        self.elem = element
    
class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def add(self, elem) -> None:
        newElem = Element(elem)
        self.size += 1
        if self.head is None:
            self.head = newElem
            return
        lastELem = self.head
        while lastELem.next != None:
            lastELem = lastELem.next
        lastELem.next = newElem
        return

    def get(self, index):
        counter = 0
        lastElem = self.head
        if index >= self.size or index < 0:
                return IndexError("Out of range")
        while counter != index:
            lastElem = lastElem.next
            counter += 1
        return lastElem.elem

    def __str__(self) -> str:
        index = self.head
        result = ''
        while index.next != None:
            result += str(index.elem) + ' '
            index = index.next
        result += str(index.elem)
        return result

    def reverse(self, tail = None):
        print(self.head.elem, self.head.next, tail)
        while self.head:
            self.head.next, tail, self.head = tail, self.head, self.head.next
        self.head = tail


if __name__=='__main__':
    arr = LinkedList()
    arr.add(10)
    arr.add(11)
    arr.add(12)
    arr.add(13)
    print(arr)
    arr.reverse()
    print(arr)
