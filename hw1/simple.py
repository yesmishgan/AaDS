import math

def isSimple(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

if __name__=='__main__':
    number = int(input())
    print(isSimple(number))