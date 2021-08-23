
def solution1(n,moves):
    x = 1
    y = 1

    for i in moves:
        if i is 'R':
            if y != n: y += 1
        elif i is 'U':
            if x != 1: x += 1
        elif i is 'D':
            if x != n: x += 1
        elif i is 'L':
            if y != 1: y += 1

    print(x,y)

def solution2(n):
    result = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    result+=1
    return result

def solution3(position):
    row = int(position[1])
    col = int(ord(position[0])) - int(ord('a')) +1
    result = 0
    steps =[(-2,-1),(-1,-2),(-2,1),(-1,2),(2,-1),(1,-2),(2,1),(1,2)]

    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]
        if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8 :
            result += 1
    return result

solution1(5,['R','R','R','U','D','D'])
print("****")
print(solution2(5))
print("****")
print(solution3("a1"))
print(solution3("c3"))