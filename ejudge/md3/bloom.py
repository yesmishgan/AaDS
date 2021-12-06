import re
import sys
from math import ceil
import math

MERCEN = 2147483647

class BitArray():

    def __init__(self, size) -> None:
        self.__array = bytearray(math.ceil(size/8))

    def set_true(self, bit) -> None:
        self.__array[bit // 8] |= 2 ** (bit % 8)

    def get_value(self, bit) -> bool:
        x = self.__array[bit // 8]
        value = x & (2 ** (bit % 8))
        return value


class BloomFilter:
    def __init__(self, n, P) -> None:
        self.__m = round(-n * math.log2(P) / math.log(2))
        self.__k = round(-math.log2(P))
        self.__primes = []
        self.__primes_list()
        self.__arr = BitArray(self.__m)

    # Internal methods

    def __primes_list(self) -> None:
        number = 2
        while len(self.__primes) < self.__k:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    break
            else:
                self.__primes.append(number)
            number += 1

    # External methods

    def add(self, K) -> None:
        for i in range(self.__k):
            h = (((i + 1) * K + self.__primes[i]) % MERCEN) % self.__m
            self.__arr.set_true(h)

    def search(self, K) -> bool:
        for i in range(self.__k):
            h = (((i + 1) * K + self.__primes[i]) % MERCEN) % self.__m
            if not self.__arr.get_value(h):
                return False
        return True

    def print(self, out = sys.stdout) -> None:
        for i in range(0, self.__m):
            if self.__arr.get_value(i):
                out.write('1')
            else:
                out.write('0')
        out.write('\n')

    def get_m(self) -> int:
        return self.__m

    def get_k(self) -> int:
        return self.__k


if __name__ == '__main__':

    bloom = None
    flag = False
    
    for line in sys.stdin:
        if re.match(r'^\s+$', line):
            continue

        if re.match(re.compile(r'(^add \d+$)'), line) and flag:
            bloom.add(int(line.split()[1]))

        elif re.match(re.compile(r'(^search \d+$)'), line) and flag:
            if bloom.search(int(line.split()[1])):
                print(1)
            else:
                print(0)
        elif re.match(re.compile(r'(^print$)'), line) and flag:
            bloom.print()

        elif re.match(re.compile(r'(^set \d+ (1|0|(0\.\d+))$)'), line) and not flag:
            
            temp = line.split()
            first = int(temp[1])
            second = float(temp[2])
            if first != 0 and round(-math.log2(second)) > 0:
                flag = True
                bloom = BloomFilter(first, second)
                print(f'{bloom.get_m()} {bloom.get_k()}')
            else:
                print('error')

        else:
            print('error')