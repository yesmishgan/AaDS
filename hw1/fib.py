def fib(n):
    a = 1
    b = 1
    c = 1
    rc = 0
    d = 0
    rd = 1
    while n>0:
        if n%2!=0:  #Если степень нечетная
            # Умножаем вектор R на матрицу A
            tc = rc
            rc = rc*a + rd*c
            rd = tc*b + rd*d
        #Умножаем матрицу A на саму себя
        ta = a
        tb = b
        tc = c
        a = a*a  + b*c
        b = ta*b + b*d
        c = c*ta + d*c
        d = tc*tb+ d*d
        n >>= 1 #Уменьшаем степень вдвое
    return rc

"""
|1 1|^n = |F_(n+1) F_n | F_1 = 1 |a b|
|1 0|     |F_n  F_(n-1)| F_2 = 1 |c d|
"""

if __name__=='__main__':
    print(fib(10))