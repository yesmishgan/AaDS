import time
import matplotlib.pyplot as plt

def exponentiation(num, n):
    res = 1
    mult = num

    while n != 0:
        if n % 2 == 1:
            res *= mult
        mult *= mult
        n = int(n / 2)
    
    return res

def stupid_exponentiation(num, n):
    res = 1
    for i in range(n):
        res *= num
    return res

if __name__=='__main__':
    inputData = [i for i in range(10000, 20000)]
    outputData1 = []
    outputData2 = []
    for i in inputData:
        startTime = time.time()
        stupid_exponentiation(2, i)
        outputData1.append(time.time() - startTime)
        startTime = time.time()
        exponentiation(2, i)
        outputData2.append(time.time() - startTime)

    plt.plot(inputData, outputData1, label = "stupid")
    plt.plot(inputData, outputData2, label = "smart")
    plt.legend()
    plt.show()