def solution4(n,m,direction):
    result = 0
    x = 1
    y = 1
    steps = [(-1,0),(0,-1),(1,0),(0,1)]
    map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
    di = direction
    visit = 0
    map[x][y] = 2
    while True:
        if visit is 4:
            break
        visit = 0
        while True:
            if visit is 4:
                break
            next_x = x+steps[di][0]
            next_y = y+steps[di][1]
            if map[next_x][next_y] is 1:
                visit += 1
            elif map[next_x][next_y] is 0:
                map[next_x][next_y] = 2
                result += 1
                break
    return result

print("****")
print(solution4(4,4,0))