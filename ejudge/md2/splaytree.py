from collections import deque
import os
import re
import sys
from typing import Set

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

    def print_nulls(self, temp):
        temp_str = '_ ' * (2 ** temp)

        return temp_str

    def print(self):
        if (self.root == None):
            print('_')
            return

        q = deque() #Вершины
        pos = deque() #Позиции, где есть узел, на уровне

        print(f'[{self.root.key} {self.root.data}]')

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
            width_level = 2 ** level
            for position in range(width_level):
                if curr == position and nums_of_nodes > 0:
                    nums_of_nodes -= 1
                    node = q.popleft()
                    if curr != width_level - 1:
                        sys.stdout.write(f'[{node.key} {node.data} {node.P.key}] ')
                    else:
                        sys.stdout.write(f'[{node.key} {node.data} {node.P.key}]')
                    if node.left != None:
                        q.append(node.left)
                        pos.append(2 * (curr + 1) - 2)
                    if node.right != None:
                        q.append(node.right)
                        pos.append(2 * (curr + 1) - 1)

                    if len(pos) != 0:
                        curr = pos.popleft()
                else:
                    sys.stdout.write('_')
                    if position != width_level - 1:
                        sys.stdout.write(' ')
            sys.stdout.write('\n')
            nums_of_nodes = len(pos) + 1   
 
            

    
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
            print('error')
            self.splay(temp)
            return
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


    def set(self, K, V):
        temp = self.__find(K)
        if temp == None:
            #self.splay(temp)
            print('error')
            return
        
        if temp.key != K:
            self.splay(temp)
            print('error')
            return
        temp.data = V
        self.splay(temp)

    def delete(self, K):
        temp = self.__find(K)
    
        if temp == None:
            print("error")
            return
        
        self.splay(temp)

        if temp.key != K:
            print("error")
            return
        
        if temp.left == None:
            self.root = temp.right
            if self.root == None:
                return
            temp.right.P = None
            return
        
        if temp.right == None:
            self.root = temp.left
            temp.left.P = None
            return

        temp.left.P = None
        tmp = temp.left
        while tmp.right != None:
            tmp = tmp.right
        self.splay(tmp)

        if temp.right != None:
            tmp.right = temp.right
            temp.right.P = tmp
        self.root = tmp
        
    def search(self, K):
        if not self.root:

            print(0)
            return
        prev = None
        tmp = self.root
        while tmp != None:
            prev = tmp
            if K == tmp.key:
                self.splay(tmp)

                print('1 ' + tmp.data)
                return
            elif K < tmp.key:
                tmp = tmp.left
            else:
                tmp = tmp.right
        self.splay(prev)
        print(0)


    def min(self):
        if not self.root:
            print("error")
            return
        
        tmp = self.root
        while tmp.left != None:
            tmp = tmp.left
        self.splay(tmp)
        print(f'{tmp.key} ' + tmp.data)

    def max(self):
        if not self.root:
            print("error")
            return
        
        tmp = self.root
        while tmp.right != None:
            tmp = tmp.right
        self.splay(tmp)
        print(f'{tmp.key} ' + tmp.data)


if __name__=='__main__':

    sys.setrecursionlimit(10000)

    tree = SplayTree()
    for line in sys.stdin:
        if line == '\n':
            continue
        
        command = line.split()
        if re.match(r'^add -?\d+ \S+$', line):
            tree.add(int(command[1]), command[2])

        elif re.match(r'^set -?\d+ \S+$', line):
            tree.set(int(command[1]), command[2])

        elif re.match(r'^delete -?\d+$', line):
            tree.delete(int(command[1]))

        elif re.match(r'^search -?\d+$', line):
            tree.search(int(command[1]))

        elif re.match(r'^min$', line):
            tree.min()
            
        elif re.match(r'^max$', line):
            tree.max()
    
        elif re.match(r'^print$', line):
            tree.print()
        
        else:
            print("error")
