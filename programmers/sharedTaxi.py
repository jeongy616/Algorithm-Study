import math

def solution(n, s, a, b, fares):
    answer = 9876543210
    g = [[9876543210] * (n) for i in range(n)]

    for f in fares:
        g[f[0] - 1][f[1] - 1] = f[2]
        g[f[1] - 1][f[0] - 1] = f[2]

    for i in range(n):
        g[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    for i in range(n):
        answer = min(answer, g[s - 1][i] + g[i][b - 1] + g[i][a - 1])

    return answer

print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))