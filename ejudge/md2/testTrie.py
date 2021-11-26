import sys
from collections import deque, defaultdict

class Trie:     

    def __init__(self):
        self.word = None # Все время None за исключением конца слова, переходя по цепочке дерева
        self.nodes = {}

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.nodes: 
                node.nodes[letter] = Trie()

            node = node.nodes[letter]

        node.word = word # Помечаем конец вставляемого слова

    def autocorrection(self, incorrect_word: str, k=1) -> list:
            """
            Функция определяет набор слов из BK-дерева, правописание которых схоже со входным словом
            :param incorrect_word: слово для проверки правильности его написания
            :param k: дистанция редактирования; максимально количество ошибок, допущенных во входном слове(по умолчанию равно 1)
            :return: список слов, правописание которых похоже на входное;
            если входное слово написано правильно - возвращает "ok", если не удалось найти похожие слова - возвращает - "?"
            """
            """if self.__root is None:
                return []"""

            answer = []
            queue = deque()
            queue.append(self)
            while len(queue) != 0:
                curr_node = queue.popleft()
                if curr_node.word == incorrect_word.lower():
                    return [incorrect_word]

                dist = self.__damerau_levenshtein(incorrect_word.lower(), curr_node.word)
                if dist <= k:
                    answer.append(curr_node.word)
                for i in curr_node.children:
                    if dist - k <= i <= dist + k:
                        '''
                        Чтобы минимизировать время поиска точного совпадения с входным словом в BK-дереве, посещаем при 
                        обходе сначала те вершины, которые могут его содержать это слово. 
                        Для текущего узла таким является только дочерний узел с таким же расстоянием Дамерау-Левенштейна,
                        что и текущий узел.
                        '''
                        if i == dist:
                            queue.appendleft(curr_node.children[i])
                        else:
                            queue.append(curr_node.children[i])

            if len(answer) == 0:
                return []
            else:
                return answer

    @staticmethod
    def __damerau_levenshtein(word1: str, word2: str) -> int:
            """
            Функция определяет расстояние Дамерау-Левенштейна между двумя строками.
            Используется корректный(не упрощённый) алгоритм расчёта.
            :param word1: первое слово для расчёта расстояния
            :param word2: второе слово для расчёта расстояния
            :return: расстояние Дамерау-Левенштейна
            """
            len_word1 = len(word1)
            len_word2 = len(word2)
            max_dist = len_word1 + len_word2
            alph_dict = defaultdict(int)  # словарь встреченных букв в слове word1 с указание позиции буквы в слове

            dist_matrix = [[0] * (len_word2 + 2) for i in range(len_word1 + 2)]

            for i in range(len_word1 + 1):
                dist_matrix[i + 1][1] = i
                dist_matrix[i + 1][0] = max_dist

            for j in range(len_word2 + 1):
                dist_matrix[1][j + 1] = j
                dist_matrix[0][j + 1] = max_dist

            dist_matrix[0][0] = max_dist

            for i in range(1, len_word1 + 1):
                letter_pos = 0
                for j in range(1, len_word2 + 1):
                    k = alph_dict[word2[j - 1]]
                    l = letter_pos
                    value = 1
                    if word1[i - 1] == word2[j - 1]:
                        value = 0
                        letter_pos = j
                    dist_matrix[i + 1][j + 1] = min(
                        dist_matrix[i][j] + value,  # замена
                        dist_matrix[i + 1][j] + 1,  # вставка
                        dist_matrix[i][j + 1] + 1,  # удаление
                        dist_matrix[k][l] + (i - k - 1) + 1 + (j - l - 1))  # транспозиция
                alph_dict[word1[i - 1]] = i
            return dist_matrix[len_word1 + 1][len_word2 + 1]


if __name__=="__main__":
    trie = Trie()
    n = int(input())
    for i in range(n):
        trie.insert(input().lower())
    
    for line in sys.stdin:
        if line == '\n':
            continue
        line = line[:-1]
        results = trie.autocorrection(line.lower(), 1)
        length = len(results)

        if length == 0:
            print(line, '-?')
        elif length == 1:
            if results[0][1] == 0:
                print(line, '- ok')
            else:
                print(line, '->', results[0][0])
        elif (line, 0) in results:
            print(line, '- ok')
        else:
            sys.stdout.write(line + ' -> ')
            for i in range(length-1, -1, -1):
                sys.stdout.write(results[i][0])
                if i != 0:
                    sys.stdout.write(', ')
                else:
                    sys.stdout.write('\n')