def change(money):
    unit = [500, 100, 50, 10]
    result = 0
    for i in unit:
        tmp = money / i
        money -= (i*tmp)
        result += tmp

    return result

def maxNum(n,m,k,nums):
    nums.sort(reverse=True)
    result = 0

    for i in range(m):
        if (i+1)%k == 0:
            result += nums[1]
        else:
            result += nums[0]
    return result

def cardGame(n,m,cards):
    result = 0
    for i in range(n):
        tmp = cards[i].sort()
        if result < cards[i][0]:
            result = cards[i][0]
    return result

def untilNumOne(n,k):
    result = (n%k)
    while n > 1:
        n = n / k
        result += 1

    return result

print("==== Min Change ====")
print(change(1260))
print("===Max Number ===")
print(maxNum(5,8,3,[2,4,5,4,6]))
print(maxNum(5,7,2,[3,4,3,4,3]))
print("=== Number Card Game ====")
print(cardGame(3,3,[[3,1,2],[4,1,4],[2,2,2]]))
print(cardGame(2,4,[[7,3,1,8],[3,3,3,4]]))
print("=== Until it becomes 1 ===")
print(untilNumOne(17,4))
print(untilNumOne(25,5))