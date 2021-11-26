from collections import deque
import sys


class Vertex:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def make_right_child(self, x, r):
        x.right = r
        if r == None:
            return
        x.right.parent = x

    def make_left_child(self, x, l):
        x.left = l
        if l == None:
            return
        x.left.parent = x

    def right_rotation(self, x):
        ex_x_right = x.right
        ex_x_parent = x.parent
        if x.parent.parent == None:
            self.root = x
            x.parent = None
        elif x.parent.parent.right == x.parent:
            self.make_right_child(x.parent.parent, x)
        else:
            self.make_left_child(x.parent.parent, x)
        self.make_right_child(x, ex_x_parent)
        self.make_left_child(x.right, ex_x_right)
        return

    def left_rotation(self, x):
        ex_x_left = x.left
        ex_x_parent = x.parent
        if x.parent.parent == None:
            self.root = x
            x.parent = None
        elif x.parent.parent.right == x.parent:
            self.make_right_child(x.parent.parent, x)
        else:
            self.make_left_child(x.parent.parent, x)
        self.make_left_child(x, ex_x_parent)
        self.make_right_child(x.left, ex_x_left)

    def splay(self, x):
        if x == None:
            return
        while (x.parent != None):
            grandpa = x.parent.parent
            if grandpa == None:
                if x.parent.left == x:
                    self.right_rotation(x)
                else:
                    self.left_rotation(x)
            elif grandpa.right == x.parent and x.parent.right == x:
                self.left_rotation(x.parent)
                self.left_rotation(x)
            elif grandpa.left == x.parent and x.parent.left == x:
                self.right_rotation(x.parent)
                self.right_rotation(x)
            elif grandpa.right == x.parent and x.parent.left == x:
                self.right_rotation(x)
                self.left_rotation(x)
            else:
                self.left_rotation(x)
                self.right_rotation(x)
        return

    def find(self, K):
        if self.root == None:
            return None
        tmp = self.root
        while tmp != None:
            if tmp.key > K:
                tmp = tmp.left
            elif tmp.key < K:
                tmp = tmp.right
            else:
                return tmp
        return None

    def add(self, K, V):
        this_ver = Vertex(K, V)
        if self.root == None:
            self.root = this_ver
            return False
        tmp = self.find(K)
        if tmp != None:
            self.splay(tmp)
            return True
        prev = None
        curr = self.root
        while curr != None:
            prev = curr
            if K > curr.key:
                curr = curr.right
            else:
                curr = curr.left
        if K > prev.key:
            self.make_right_child(prev, this_ver)
        else:
            self.make_left_child(prev, this_ver)

        self.splay(this_ver)
        return False

    def set(self, K, V):

        tmp = self.search(K)
        if tmp == None:
            return True
        tmp.data = V
        return False

    def max(self):
        if not self.root:
            return None
        curr = self.root
        prev = None
        while curr:
            prev = curr
            curr = curr.right
        self.splay(prev)
        return prev

    def merge(self, left_root, right_root):
        if not left_root and not right_root:
            self.root = None
        if not left_root:
            self.root = right_root
        elif not right_root:
            self.root = left_root
        else:
            self.root = left_root
            self.max()
            self.make_right_child(self.root, right_root)
            self.root.parent = None

    def delete(self, K):
        tmp = self.search(K)

        if tmp == None:
            return True
        if tmp.left != None:
            tmp.left.parent = None
        if tmp.right != None:
            tmp.right.parent = None

        self.merge(tmp.left, tmp.right)
        return False

    def search(self, K):
        if not self.root:
            return None
        prev = None
        curr = self.root
        while curr != None:
            prev = curr
            if K == curr.key:
                self.splay(curr)
                return curr
            elif curr.key > K:
                curr = curr.left
            elif curr.key < K:
                curr = curr.right
        self.splay(prev)
        return None

    def min(self):
        if not self.root:
            return None
        curr = self.root
        prev = None
        while curr:
            prev = curr
            curr = curr.left
        self.splay(prev)
        return prev

    def height(self, vert):
        if vert is None:
            return 0
        return 1 + max(self.height(vert.left), self.height(vert.right))

    def print(self, out=sys.stdout):
        if self.root is None:
            out.write('_\n')
            return
        out.write('[' + str(self.root.key) + ' ' + self.root.data + ']\n')
        que = deque()
        pos = deque()
        if self.root.left != None:
            pos.append(0)
            que.append(self.root.left)
        if self.root.right != None:
            pos.append(1)
            que.append(self.root.right)
        height_of_tree = self.height(self.root)
        vert_num = len(pos)
        if vert_num == 0:
            return
        curr = pos.popleft()
        for level in range(1, height_of_tree):
            curr_pos = 0
            width = 2 ** level
            while vert_num != 0:
                if curr_pos == curr:
                    vert = que.popleft()
                    vert_num -= 1
                    out.write('[' + str(vert.key) + ' ' + vert.data + ' ' + str(vert.parent.key) + ']')
                    if curr != width - 1:
                        out.write(' ')
                    if vert.left != None:
                        pos.append(2 * (curr + 1) - 2)
                        que.append(vert.left)
                    if vert.right != None:
                        pos.append(2 * (curr + 1) - 1)
                        que.append(vert.right)
                    curr_pos = curr + 1
                    if len(pos) != 0:
                        curr = pos.popleft()
                elif curr - curr_pos != 0:
                    out.write('_ ' * (curr - curr_pos))
                    curr_pos = curr
                if vert_num == 0:
                    out.write('_ ' * (width - curr_pos - 1))
                    if curr_pos != width:
                        out.write('_')
            vert_num = len(pos) + 1
            sys.stdout.write('\n')


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    tree = SplayTree()
    for line in sys.stdin:
        if line == '\n':
            continue

        if len(line) < 3:
            print('error')
            continue
        if line[0] == ' ':
            print('error')
            continue
        if line[-2] == ' ':
            print('error')
            continue
        command = line.split()
        if command[0] == 'print' and len(command) == 1:
            tree.print()
        elif command[0] == 'max' and len(command) == 1:
            res = tree.max()
            if res is None:
                print('error')
            else:
                print(str(res.key) + ' ' + res.data)
        elif command[0] == 'min' and len(command) == 1:
            res = tree.min()
            if res is None:
                print('error')
            else:
                print(str(res.key) + ' ' + res.data)

        elif len(command) == 3 and command[0] == 'add':
            res = tree.add(int(command[1]), command[2])
            if res:
                print('error')

        elif len(command) == 3 and command[0] == 'set':
            res = tree.set(int(command[1]), command[2])
            if res:
                print('error')
        elif len(command) == 2 and command[0] == 'delete':
            res = tree.delete(int(command[1]))
            if res:
                print('error')
        elif len(command) == 2 and command[0] == 'search':
            res = tree.search(int(command[1]))
            if res is None:
                print('0')
            else:
                print('1 ' + res.data)
        else:
            print('error')
