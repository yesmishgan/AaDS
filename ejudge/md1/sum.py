from os import read
import sys

input = []

flag = True
idx = 0
res = ''
for index, elem in enumerate(sys.stdin.read()):
    if elem.isnumeric():
        res += elem
    elif elem == "-" and len(res) == 0:
        res += elem
    else:
        input.append(res)
        res = ''
input = [int(x) for x in input if x and x != '-']
print(sum(input))