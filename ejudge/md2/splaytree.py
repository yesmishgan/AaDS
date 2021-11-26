from collections import deque
import os
import re
import sys

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data

        self.P = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self) -> None:
        self.root = None

    def __rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != None:
            left_child.right.P = node

        left_child.P = node.P
        if node.P == None:
            self.root = left_child
        elif node == node.P.right:
            node.P.right = left_child
        else:
            node.P.left = left_child

        left_child.right = node
        node.P = left_child

    def __rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != None:
            right_child.left.P = node

        right_child.P = node.P
        if node.P == None:
            self.root = right_child
        elif node == node.P.left:
            node.P.left = right_child
        else:
            node.P.right = right_child
        right_child.left = node
        node.P = right_child

    def splay(self, node):
        while node.P != None:
            if node == node.P.left:
                if node.P.P == None:
                    self.__rotate_right(node.P)
                elif node.P.P.left == node.P:
                    self.__rotate_right(node.P.P)
                    self.__rotate_right(node.P)
                else:
                    self.__rotate_right(node.P)
                    self.__rotate_left(node.P)
            else:
                if node.P.P == None:
                    self.__rotate_left(node.P)
                elif node.P.P.right == node.P:
                    self.__rotate_left(node.P.P)
                    self.__rotate_left(node.P)
                else:
                    self.__rotate_left(node.P)
                    self.__rotate_right(node.P)

    def print(self, out=sys.stdout):
        if (self.root == None):
            out.write('_\n')
            return

        q = deque() #Вершины
        pos = deque() #Позиции, где есть узел, на уровне

        out.write(f'[{self.root.key} {self.root.data}]\n')

        if self.root.left != None:
            q.append(self.root.left)
            pos.append(0)

        if self.root.right != None:
            q.append(self.root.right)
            pos.append(1)

        height = self.__height(self.root)
        nums_of_nodes = len(pos)
        if nums_of_nodes == 0:
            return
        curr = pos.popleft()
        
        for level in range(1, height):
            curr_pos = 0
            width_level = 2 ** level
            while nums_of_nodes != 0:
                if curr_pos == curr:
                    nums_of_nodes -= 1
                    node = q.popleft()
                    if curr != width_level - 1:
                        out.write(f'[{node.key} {node.data} {node.P.key}] ')
                    else:
                        out.write(f'[{node.key} {node.data} {node.P.key}]')
                    if node.left != None:
                        q.append(node.left)
                        pos.append(2 * (curr + 1) - 2)
                    if node.right != None:
                        q.append(node.right)
                        pos.append(2 * (curr + 1) - 1)
                    curr_pos = curr + 1
                    if len(pos) != 0:
                        curr = pos.popleft()
                elif curr - curr_pos != 0:
                    out.write('_ ' * (curr - curr_pos))
                    curr_pos = curr
                if nums_of_nodes == 0:
                    out.write('_ ' * (width_level - curr_pos - 1))
                    if curr_pos != width_level:
                        out.write('_')
            nums_of_nodes = len(pos) + 1
            out.write('\n')

            

    
    def __height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__height(node.left), self.__height(node.right))


    def __find(self, K):
        if not self.root:
            return None
        prev = None
        tmp = self.root
        while tmp != None:
            prev = tmp
            if K == tmp.key:

                return tmp
            elif K < tmp.key:
                tmp = tmp.left
            else:
                tmp = tmp.right

        return prev

    def add(self, K, V):
        temp = self.__find(K)
        if temp != None and temp.key == K:
            self.splay(temp)
            return False
        new_elem = Node(K, V)
        prev = None
        curr = self.root
        while curr != None:
            prev = curr
            if K < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        new_elem.P = prev
        if prev == None:
            self.root = new_elem
        elif new_elem.key > prev.key:
            prev.right = new_elem
        else:
            prev.left = new_elem

        self.splay(new_elem)
        return True


    def set(self, K, V):
        temp = self.__find(K)
        if temp == None:
            return False
        
        if temp.key != K:
            self.splay(temp)
            return False
        temp.data = V
        self.splay(temp)
        return True

    def delete(self, K):
        temp = self.__find(K)
    
        if temp == None:
            return False
        
        self.splay(temp)

        if temp.key != K:
            return False
        
        if temp.left == None:
            self.root = temp.right
            if self.root == None:
                return True
            temp.right.P = None
            return True
        
        if temp.right == None:
            self.root = temp.left
            temp.left.P = None
            return True

        temp.left.P = None
        tmp = temp.left
        while tmp.right != None:
            tmp = tmp.right
        self.splay(tmp)

        if temp.right != None:
            tmp.right = temp.right
            temp.right.P = tmp
        self.root = tmp
        return True
        
    def search(self, K):
        if not self.root:
            return None
        prev = None
        tmp = self.root
        while tmp != None:
            prev = tmp
            if K == tmp.key:
                self.splay(tmp)
                return tmp
            elif K < tmp.key:
                tmp = tmp.left
            else:
                tmp = tmp.right
        self.splay(prev)
        return None


    def min(self):
        if not self.root:
            return None
        
        tmp = self.root
        while tmp.left != None:
            tmp = tmp.left
        self.splay(tmp)
        return tmp

    def max(self):
        if not self.root:
            return None
        
        tmp = self.root
        while tmp.right != None:
            tmp = tmp.right
        self.splay(tmp)
        return tmp


if __name__=='__main__':

    sys.setrecursionlimit(10000)

    tree = SplayTree()
    for line in sys.stdin:
        if line == '\n':
            continue
        
        command = line.split()
        if re.match(r'^add -?\d+ \S+$', line):
            result = tree.add(int(command[1]), command[2])
            if not result:
                print("error")

        elif re.match(r'^set -?\d+ \S+$', line):
            result = tree.set(int(command[1]), command[2])
            if not result:
                print("error")

        elif re.match(r'^delete -?\d+$', line):
            result = tree.delete(int(command[1]))
            if not result:
                print("error")

        elif re.match(r'^search -?\d+$', line):
            result = tree.search(int(command[1]))
            if result != None:
                print('1 ' + result.data)
            else:
                print(0)

        elif re.match(r'^min$', line):
            result = tree.min()
            if result != None:
                print(f'{result.key} ' + result.data)
            else:
                print('error')
            
        elif re.match(r'^max$', line):
            result = tree.max()
            if result != None:
                print(f'{result.key} ' + result.data)
            else:
                print('error')
    
        elif re.match(r'^print$', line):
            tree.print()
        
        else:
            print("error")
