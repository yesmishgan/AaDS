def rich_bitch_game(cash):
    num = 0
    while cash != 0: # идем в обратном порядке операций до 0
        if cash % 2 == 0: # операция dbl
            num += 1
            cash //= 2

        if cash == 1: # операция inc
            num += 1
            cash -= 1

        if cash % 2 == 1:
            way_first = bin(cash + 1)[2:]
            way_second = bin(cash - 1)[2:]
            
            if way_first.count('1') < way_second.count('1'): # операция dec
                cash += 1

            elif way_first.count('1') == way_second.count('1'):
			    
                length = len(way_first)//2

                for i in range(length, len(way_first) - 1):
                    if way_first[i] > way_second[i]: # операция dec
                        cash += 1
                        break
                    if way_first[i] < way_second[i] or len(way_second) < len(way_first): # операция inc
                        cash -= 1
                        break
            else: # операция inc
                cash -= 1
            num += 1
    return num
            
if __name__=="__main__":
    cash = int(input())
    print(rich_bitch_game(cash))