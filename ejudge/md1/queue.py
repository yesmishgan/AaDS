import re
import sys

queue = []
head = 0
size = 0
tail = -1
capacity = -1
queue_exist = False


input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

if __name__=="__main__":
    for line in input.readlines():
        flag = False

        if line == '\n':

            flag = True

        if re.match(r'^(set_size)\s[0-9]*$', line):

            flag = True

            if not queue_exist:
                queue_exist = True
                capacity = int(line[9:-1])
                queue = [None] * capacity
            else:
                output.write("error\n")

        if re.match(r'^push\s\S*$', line):

            flag = True

            if not queue_exist:
                output.write("error\n")
                continue
            if size + 1 <= capacity:
                tail = (tail + 1) % capacity
                queue[tail] = line[5:-1]
                size += 1
            else:
                output.write("overflow\n")
        
        if re.match(r'^(pop)$', line):

            flag = True

            if not queue_exist:
                output.write("error\n")
                continue
            if size == 0:
                output.write('underflow\n')
                continue
            output.write(queue[head] + '\n')
            head = (head + 1) % capacity
            size -= 1
                

        if re.match(r'^(print)$', line):
            flag = True

            if not queue_exist:
                output.write("error\n")
                continue
            if size == 0:
                output.write('empty\n')
                continue
            if head <= tail:
                output.write(' '.join(map(str, queue[head:tail + 1])) + '\n')
            else:
                output.write(' '.join(map(str, queue[head:] + queue[:tail + 1])) + '\n')
        if not flag:
            output.write("error\n")