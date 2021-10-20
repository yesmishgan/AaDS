import re
from sre_constants import error
import sys

stack = []
size = -1
capacity = -1
stack_exist = False
#result = []

if __name__=="__main__":
    for line in sys.stdin:

        flag = False

        if line == '\n':

            flag = True

        if re.match(r'^(set_size)\s[0-9]*$', line):

            flag = True

            if not stack_exist:
                stack_exist = True
                capacity = int(line[9:-1])
                stack = [None] * capacity
            else:
                print("error")
                #result.append("error")

        if re.match(r'^push\s\S*$', line):

            flag = True

            if not stack_exist:
                print("error")
                #result.append("error")
                continue
            if size + 1 < capacity:
                stack[size + 1] = line[5:-1]
                size += 1
            else:
                print("overflow")
                #result.append("overflow")
        
        if re.match(r'^pop$', line):

            flag = True

            if not stack_exist:
                print('error')
                #result.append("error")
                continue
            if size == -1:
                print('underflow')
                #result.append("underflow")
                continue
            print(stack[size])
            #result.append(stack[size])
            stack[size] = None
            size -= 1

        if re.match(r'^(print)$', line):

            flag = True

            if not stack_exist:
                print('error')
                #result.append("error")
                continue
            if size == -1:
                print('empty')
                #result.append("empty")
                continue
            print(' '.join(stack[0: size + 1]))
            #result.append(' '.join(stack[0: size + 1]))
        if not flag:
            print("error")
            #result.append("error")

"""
    for elem in result:
        print(elem)
"""