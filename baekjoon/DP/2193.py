def solution(n):
    binArr = [0] * (n + 1)
    binArr[1] = 1
    if n > 1:
        binArr[2] = 1
        for i in range(3, n + 1):
            binArr[i] = binArr[i - 1] + binArr[i - 2]
    print(binArr[n])


n = int(input())
solution(n)