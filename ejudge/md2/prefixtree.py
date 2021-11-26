import os
import sys

class Trie:
    def __init__(self) -> None:
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if node.get(char) == None:
                node[char] = {}
            node = node[char]
    
    def find(self, word):
        pass


if __name__=='__main__':
    trie = Trie()
    n = int(input())
    for i in range(n):
        trie.insert(input().lower())

    for word in sys.stdin:
        if word == '\n':
            continue
        trie.find(word)
    
"""class Corrector:
    def __init__(self):
        self.dict = {}

    def add(self, word):
        if self.dict.get(len(word), None):
            self.dict[len(word)].append(word)
        else:
            self.dict[len(word)] = [word]        

    def check(self, word):
        dict_words = []
        word = word.lower()
        temp = self.dict.get(len(word), None)
        if temp:
            for i in temp:
                dist = self.dist(word, i)
                if dist >= 0 and dist <= 1:
                    dict_words.append((i, dist))

        temp = self.dict.get(len(word) + 1, None)
        if temp:
            for i in temp:
                dist = self.dist(word, i)
                if dist >= 0 and dist <= 1:
                    dict_words.append((i, dist))

        temp = self.dict.get(len(word) - 1, None)
        if temp:
            for i in temp:
                dist = self.dist(word, i)
                if dist >= 0 and dist <= 1:
                    dict_words.append((i, dist))

        dict_words.sort()
        return dict_words

    def dist(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            temp = s1
            s1 = s2
            s2 = temp
            temp = len1
            len1 = len2
            len2 = temp

        previous = None
        current = []
        for i in range(len1 + 1):
            current.append(i)

        for i in range(1, len2 + 1):
            transp = previous
            previous = current
            current = [0] * (len1 + 1)
            current[0] = i

            if transp:
                cont = False
                for temp in transp:
                    if temp <= 1:
                        cont = True
                if not cont:
                    return -1

            for j in range(1, len1 + 1):
                if s1[j - 1] == s2[i - 1]:
                    cost = 0
                else:
                    cost = 1

                current[j] = min(current[j - 1] + 1, previous[j] + 1, previous[j - 1] + cost)

                if i > 1 and i <= j:
                    if s1[j - 1] == s2[j - 2]:
                        if s1[j - 2] == s2[j - 1]:
                            current[j] = min(current[j], transp[j - 2] + 1)
        return current[-1]


def emptyLine(line):
    line.replace(' ', '')
    if line:
        return False
    return True


try:
    N = int(input())

    dictionary = Corrector()
    for i in range(N):
        word = input().lower()
        if emptyLine(word):
            continue
        dictionary.add(word)

    cycle = True
    while cycle:
        try:
            word = input()
            if emptyLine(word):
                continue

            dict_words = dictionary.check(word)
            if dict_words == []:
                print(word, '-?')
                continue

            out = word + ' -> '
            found = False
            for i in dict_words:
                if i[1] == 0:
                    print(word, '- ok')
                    found = True
                    break
                out += i[0] + ', '
            if not found:
                print(out[0:-2])

        except Exception:
            cycle = False

except Exception:
    print('error')"""