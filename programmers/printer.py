from collections import deque

def solution(priorities, location):
    p = {}
    position = []

    for i in range(1, len(priorities) + 1):
        p[i] = priorities[i - 1]

    que = deque(p)
    while que:
        maxVal = max(priorities)
        tmp = que.popleft()
        if p[tmp] != maxVal:
            que.append(tmp)
        else:
            position.append(tmp)
            priorities.remove(p[tmp])

    return position.index(location+1)+1

# print(solution([2,1,3,2],2)) # result : 1
print(solution([1,1,9,1,1,1],0)) # result : 5