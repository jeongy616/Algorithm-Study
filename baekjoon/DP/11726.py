def solution(n):
    tileArr = [0] * (n + 1)
    tileArr[1] = 1
    if n > 1:
        tileArr[2] = 2
        for i in range(3 , n+1):
            tileArr[i] = tileArr[i-1] + tileArr[i-2]

    print(tileArr[n] % 10007)

n = int(input())
solution(n)