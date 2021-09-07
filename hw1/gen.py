def genSub(n):
    arr = [x for x in range(1, n+1)]
    print(arr)
    copyArr = arr[:]
    a = arr[-1]
    while arr != copyArr[::-1]:
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i+1]:
                a = i
                break
        for j in range(n - 1, a, -1):
            if arr[j] > arr[a]:
                arr[j], arr[a] = arr[a], arr[j]
                break
        for i in range(a+1, a+1+int((n - (a+1))/2)):
            arr[i], arr[n + a - i] = arr[n+a-i], arr[i]
        print(arr)

if __name__=='__main__':
    genSub(5)