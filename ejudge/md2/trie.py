import sys



"""
Про автокоррекцию

Если рассматривать алгоритм Дамерау-Левенштейна в отрыве от
префиксного дерева и сравнивать произвольное введенное слово
со всеми словами из словаря, поочередно применяя функцию,
в которой описан алгоритм Дамерау-Левенштейна, то временная
сложность такого алгоритма будет составлять О(n * m^2), где
    n - количество слов с словаре
    m - длина максимального слова

В нашем случае с применением префиксного дерева
мы сводим временную сложность к О(n * m), где
    n - количество узлов в префиксном дереве
    m - длина максимального слова

Так как для каждого узла мы создаем только одну строку таблицы.
В то время как в первом случае мы каждый раз с нуля формируем таблицу

Может показаться, что вторая сложность больше.
Однако она достигает первую только если не будет ни одного пересечения
узлов у двух любых слов из словаря, находящихся в префиксном дереве.
То есть каждый узел префиксного дерева будет описывать символ только для
одного слова

Пример:
может быть три слова (hell, hello, help)
(6 узлов, но всего символов, если считать у каждого слова 13 символов)
h->e->l->l->o
       ->p

может быть три слова (hello, some, cats)
(13 символов и 13 узлов)
   -> h->e->l->l->o
"" -> s->o->m->e
   -> c->a->t->s
"""

"""
Сложность по памяти также напрямую будет зависеть от того, сколько у нас узлов в полученном префиксном дереве
Так как работает рекурсивная функция, стек вызовов наполняется. А число вызовов зависит от количества узлов.
Причем на каждом этапе мы формируем три строки равные длине слова.
Тогда сложность по памяти для автокоррекции составляет О(n * m), где m - максимальная длина слова
                                                                     n - количество узлов
"""

"""
Про вставку в префиксное дерево

Спускаемся по уровням дерева и проверяем наличие или добавляем символ. В сумме n раз

Временная сложность O(n), где n - длина вставляемого слова
Сложность по памяти O(n), где n - длина вставляемого слова
"""

"""

"""
class Trie:     

    def __init__(self):
        self.word = None
        self.nodes = {}

    def __search(self, node, character, word, previous_row, results, max_ops, prev_character=None, prevprev_row=None):

        columns = len(word) + 1
        current_row = [previous_row[0] + 1]

        for column in range(1, columns):

            insert_cost = current_row[column - 1] + 1

            delete_cost = previous_row[column] + 1

            if word[column - 1] != character:
                replace_cost = previous_row[column - 1] + 1
            else:                
                replace_cost = previous_row[column - 1]

            if word[column - 1] == prev_character and word[column - 2] == character and column > 1:
                transposition_cost = min(prevprev_row[column - 2] + 1, previous_row[column - 1])
                current_row.append(min( insert_cost, delete_cost, replace_cost, transposition_cost))
            else:                
                current_row.append(min( insert_cost, delete_cost, replace_cost))

        prev_character = character

        if current_row[-1] <= max_ops and node.word != None:
            results.append(node.word)

        if min( current_row ) <= max_ops:
            for character in node.nodes:
                self.__search(node.nodes[character], character, word, current_row, 
                    results, max_ops, prev_character, previous_row)

    def insert( self, word ):
        node = self
        for character in word:
            if character not in node.nodes: 
                node.nodes[character] = Trie()

            node = node.nodes[character]
        node.word = word

    def search(self, word):

        node = self
        for elem in word:
            res = node.nodes.get(elem)
            if res == None:
                return False
            else:
                node = res
        if node.word == word:
            return True
        return False

    def autocomlete(self, word, max_ops=1):
        current_row = range(len(word) + 1)

        results = []

        for character in self.nodes:
            self.__search(self.nodes[character],
                                 character, word, current_row, 
                                 results, max_ops)

        return results


if __name__=="__main__":
    trie = Trie()
    n = int(input())
    for i in range(n):
        trie.insert(input().lower())
    
    for line in sys.stdin:
        if line == '\n':
            continue

        line = line[:-1]
        if trie.search(line.lower()):
            print(line, '- ok')
            continue
        results = trie.autocomlete(line.lower())
        length = len(results)
        if length == 0:
            print(line, '-?')
        elif length == 1:
            if results[0] == line.lower():
                print(line, '- ok')
            else:
                print(line, '->', results[0])
        else:
            results = sorted(results, reverse=True)
            sys.stdout.write(line + ' -> ')
            for i in range(length-1, -1, -1):
                sys.stdout.write(results[i])
                if i != 0:
                    sys.stdout.write(', ')
                else:
                    sys.stdout.write('\n')