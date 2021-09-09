tmp = []
AllCourse = {}
answer = []

def addCourse(str):
    a = str.split(" ")
    a.sort()
    tmpstr = "".join(a)
    if AllCourse.__contains__(tmpstr):
        AllCourse[tmpstr] += 1
    else:
        AllCourse[tmpstr] = 1

def comb(order, n, r, start, visited):
    if r == 0:
        str = " ".join(tmp)
        addCourse(str)
        return

    for idx in range(start, n):
        if not visited[idx]:
            visited[idx] = True
            tmp.append(order[idx])
            comb(order, n, r - 1, idx + 1, visited)
            visited[idx] = False
            tmp.pop()

def maxCourse():
    maxCnt = 2
    l = sorted(AllCourse.items(),key=lambda x: x[1], reverse=True)
    print(l)
    for i in l:
        if i[1] >= maxCnt:
            maxCnt = i[1]
            answer.append(i[0])
        else:
            break

def solution(orders, course):
    for i in course:
        for j in orders:
            if i <= len(j) : comb(j, len(j), i, 0, [False] * len(j))
        maxCourse()
        AllCourse.clear()

    answer.sort()
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))