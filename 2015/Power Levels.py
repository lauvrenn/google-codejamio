import math
lines = int(input().strip())
arr = []

for i in range(0, lines):
    n = [s for s in input().split("\n")]
    arr.append(n)


def calcFact(e):
    digs = 0
    k = 0
    while((9000 - k*e) >= 2):
        digs += math.log10(9000 - k*e)
        k += 1
    return 1 + math.floor(digs)


noOfDigits = [-1]*9001
for excls in range(1, 9001):
    noOfDigits[excls] = int(calcFact(excls))


def yell(enemyDigs):
    if(enemyDigs < 4):
        return "..."
    elif(enemyDigs > 31682):
        return "IT'S OVER 9000!"

    for i in range(1, 9001):
        if(enemyDigs > noOfDigits[i]):
            return "IT'S OVER 9000" + "!"*i
    return "..."


for i in range(0, lines):
    shout = yell(int(arr[i][0]))
    print("Case #{}: ".format(i+1) + shout)

# TEST CASES
# 3
# 1
# 19
# 206
# 2
# 31682
# 31683

# searching for the number of exclamation points that will give me the number
# of digits lower than the one of the enemy

# take all input
# if enemydigits < 4 => it's not over anything
# if enemydigits > 9000! => it's over the greatest one
# if other then
# calculate if(enemydigits > number of digits of one excl point)
# if not, then increase exclamation points until we find the right number
