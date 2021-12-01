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
            way_first = bin(cash + 1)[2:]
            way_second = bin(cash - 1)[2:]
            
            if way_first.count('1') < way_second.count('1'): # операция dec
                result.append('dec')
                cash += 1

            elif way_first.count('1') == way_second.count('1'):
			    
                length = len(way_first)//2

                for i in range(length, len(way_first) - 1):
                    if way_first[i] > way_second[i]: # операция dec
                        result.append('dec')
                        cash += 1
                        break
                    if way_first[i] < way_second[i] or len(way_second) < len(way_first): # операция inc
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
    print(len(res))