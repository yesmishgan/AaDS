def binary_length(num):
    count_ones = 0
    count = 0
    while num != 0:
        count += 1
        count_ones += num % 2
        num //= 2
    return count, count_ones


def rich_bitch_game(cash):
    result = []
    while cash != 0: # идем в обратном порядке операций до 0
        if cash % 2 == 0: # операция dbl
            result.append('dbl')
            cash //= 2

        if cash == 1: # операция inc
            result.append('inc')
            cash -= 1

        if cash % 2 == 1:
            length_first, way_first = binary_length(cash + 1)
            length_second, way_second = binary_length(cash - 1)
        
            if way_first < way_second: # операция dec
                result.append('dec')
                cash += 1

            elif way_first == way_second:
			    
                length = length_first // 2

                for i in range(length - 1, -1, -1):
                    if ((cash + 1) >> i) % 2 > ((cash - 1) >> i) % 2: # операция dec
                        result.append('dec')
                        cash += 1
                        break
                    if ((cash + 1) >> i) % 2 < ((cash - 1) >> i) % 2 or length_second < length_first: # операция inc
                        result.append('inc')
                        cash -= 1
                        break
            else: # операция inc
                result.append('inc')
                cash -= 1
    return result
            
if __name__=="__main__":
    cash = int(input())
    res = rich_bitch_game(cash)[::-1]
    
    #for command in res:
    #    print(command)
    #print(len(res)) разкомментировать для автотестов