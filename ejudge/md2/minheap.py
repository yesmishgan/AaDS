import os
import re
import sys

class MinHeap:

    class Node:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value

    def __init__(self) -> None:
        self.nodes = []
        self.keys = {}

    def __parent(self, i):
        return int((i - 1) / 2)

    def __left_child(self, i):
        return 2 * i + 1

    def __right_child(self, i):
        return 2 * i + 2

    def __heapify(self, i):
        l = self.__left_child(i)
        r = self.__right_child(i)

        largest = i
        if l < len(self.nodes) and self.nodes[l].key < self.nodes[i].key:
            largest = l
        
        if r < len(self.nodes) and self.nodes[r].key < self.nodes[largest].key:
            largest = r

        if largest != i:
            self.nodes[i], self.nodes[largest] = self.nodes[largest], self.nodes[i]
            self.keys[self.nodes[i].key], self.keys[self.nodes[largest].key] = self.keys[self.nodes[largest].key], self.keys[self.nodes[i].key]
            self.__heapify(largest)

    def add(self, K, V):

        if self.keys.get(K) != None:
            return False

        self.nodes.append(self.Node(K, V))

        i = len(self.nodes) - 1
        self.keys[K] = i

        while i > 0 and self.nodes[self.__parent(i)].key > K:
            
            self.keys[self.nodes[i].key], self.keys[self.nodes[self.__parent(i)].key] = self.keys[self.nodes[self.__parent(i)].key], self.keys[self.nodes[i].key]
            self.nodes[i], self.nodes[self.__parent(i)] = self.nodes[self.__parent(i)], self.nodes[i]
            i = self.__parent(i)

        self.nodes[i] = self.Node(K, V)
        return True

    def set(self, K, V):
        idx = self.keys.get(K)
        if idx == None:
            return False
        self.nodes[idx].value = V
        return True

    def delete(self, K):
        idx = self.keys.get(K)
        if idx == None:
            return False
        
        self.keys.pop(self.nodes[idx].key)
        self.nodes[idx] = self.nodes[-1]
        self.nodes.pop()

        if idx == len(self.nodes):
            return True

        self.keys[self.nodes[idx].key] = idx

        while idx > 0 and self.nodes[self.__parent(idx)].key > self.nodes[idx].key:
            
            self.keys[self.nodes[idx].key], self.keys[self.nodes[self.__parent(idx)].key] = self.keys[self.nodes[self.__parent(idx)].key], self.keys[self.nodes[idx].key]
            self.nodes[idx], self.nodes[self.__parent(idx)] = self.nodes[self.__parent(idx)], self.nodes[idx]
            idx = self.__parent(idx)

        self.__heapify(idx)
        return True
        
    def search(self, K):
        idx = self.keys.get(K)
        if idx == None:
            return None
        return idx

    def min(self):
        if len(self.nodes) == 0:
            return None
        return self.nodes[0]

    def max(self):
        if len(self.nodes) == 0:
            return None
        max_elem = self.nodes[len(self.nodes) // 2]

        for elem in range(1 + 2 // len(self.nodes), len(self.nodes)):
            if max_elem.key < self.nodes[elem].key:
                max_elem = self.nodes[elem]
        return max_elem

    def print(self, out=sys.stdout):
        if len(self.nodes) == 0:
            out.write('_\n')
            return

        out.write(f'[{self.nodes[0].key} {self.nodes[0].value}]\n')
        if len(self.nodes) == 1:
            return
        level = 1
        curr = 1
        while True:
            width = 2 ** level
            for elem in range(width):
                if elem + curr > len(self.nodes) - 1:
                    out.write('_ ' * (width - elem - 1))
                    out.write('_')
                    break
                out.write(f'[{self.nodes[curr + elem].key} {self.nodes[curr + elem].value} {self.nodes[self.__parent(curr + elem)].key}]')
                if elem != width - 1:
                    out.write(' ')

            out.write('\n')
            curr += width
            level += 1
            if curr > len(self.nodes) - 1:
                break
                



    def extract(self):
        if len(self.nodes) == 0:
            return None
        
        node = self.nodes[0]

        self.keys.pop(self.nodes[0].key)
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()

        if len(self.nodes) == 0:
            return node 

        self.keys[self.nodes[0].key] = 0
        self.__heapify(0)
        return node


if __name__=='__main__':

    heap = MinHeap()

    for line in sys.stdin:
        if line == '\n':
            continue
        

        command = line.split()
        if re.match(r'^add -?\d+ \S+$', line):
            result = heap.add(int(command[1]), command[2])
            if not result:
                print("error")

        elif re.match(r'^set -?\d+ \S+$', line):
            result = heap.set(int(command[1]), command[2])
            if not result:
                print("error")

        elif re.match(r'^delete -?\d+$', line):
            result = heap.delete(int(command[1]))
            if not result:
                print("error")

        elif re.match(r'^search -?\d+$', line):
            result = heap.search(int(command[1]))
            if result == None:
                print(0)
            else:
                print(f'1 {result} {heap.nodes[result].value}')

        elif re.match(r'^min$', line):
            result = heap.min()
            if result == None:
                print("error")
            else:
                print(f'{result.key} {heap.keys[result.key]} {result.value}')
            
        elif re.match(r'^max$', line):
            result = heap.max()
            if result == None:
                print("error")
            else:
                print(f'{result.key} {heap.keys[result.key]} {result.value}')
    
        elif re.match(r'^extract$', line):
            result = heap.extract()
            if result == None:
                print("error")
            else:
                print(f'{result.key} {result.value}')

        elif re.match(r'^print$', line):
            heap.print()

        else:
            print("error")