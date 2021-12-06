import re
import sys
from math import gcd


class Backpack:
    def __init__(self) -> None:
        self.__capacity = 0
        self.__factor = 0
        self.__weight = 0
        self.__cost = 0
        self.__collection = []

    # Internal method to optimize table generation
    def __gcd_weights(self, weight) -> None:
        temp = weight + [self.__capacity]
        self.__factor = max(temp)
        for i in range(0, len(temp) - 1):
            if self.__factor > gcd(temp[i], temp[i + 1]):
                self.__factor = gcd(temp[i], temp[i + 1])

        for i in range(len(weight)):
            weight[i] //= self.__factor

    # Internal methods to realize algorithm
    def __find_items(self, table, weight, weight_size, capacity) -> None:
        if table[weight_size][capacity] == 0:
            return

        if table[weight_size - 1][capacity] == table[weight_size][capacity]:
            self.__find_items(table, weight, weight_size - 1, capacity)
        else:
            self.__find_items(table, weight, weight_size - 1, capacity - weight[weight_size - 1])
            self.__weight += weight[weight_size - 1] * self.__factor
            
            self.__collection.append(weight_size)

    def __gen_table(self, weight, costs) -> None:
        rows = len(weight)
        columns = self.__capacity // self.__factor
        table = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(0, columns + 1):
                if weight[i - 1] <= j:
                    table[i][j] = max(table[i - 1][j], costs[i - 1] + table[i - 1][j - weight[i - 1]])
                else:
                    table[i][j] = table[i - 1][j]

        self.__cost = table[rows][columns]
        self.__find_items(table, weight, rows, columns)

    # External methods
    def set_capacity(self, capacity) -> bool:
        if capacity >= 0:
            self.__capacity = capacity
            return True
        return False

    def calculation(self, weight, costs) -> None:
        self.__gcd_weights(weight)
        self.__gen_table(weight, costs)

    def get_collection(self) -> list:
        return self.__collection

    def get_cost(self) -> int:
        return self.__cost

    def get_weight(self) -> int:
        return self.__weight


if __name__ == '__main__':
    bag = Backpack()
    weights = []
    costs = []
    flag = False

    for line in sys.stdin:
        if line == '\n':
            continue

        if re.match(re.compile(r'(^\d+ \d+$)'), line) and flag:
            temp = line.split()
            weights.append(int(temp[0]))
            costs.append(int(temp[1]))

        elif re.match(re.compile(r'(^\d+$)'), line) and not flag:
            bag.set_capacity(int(line))
            flag = True
        else:
                print('error')
    
    # Launch computation
    bag.calculation(weights, costs)

    # Print results
    print(f'{bag.get_weight()} {bag.get_cost()}')
    for item in bag.get_collection():
        print(item)
