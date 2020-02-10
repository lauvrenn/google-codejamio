import math
lines = int(input().strip())
arr = []

for i in range(0, lines):
    n = [s for s in input().split("\n")]
    arr.append(n)


def calcFact(k, e):
    el = 9000 - k*e
    if(el < 3):
        if(el < 1):
            return 0
        return math.log10(el)
    return math.log10(el) + calcFact(k+1, e)


def noDigits(e):
    factDigs = calcFact(0, e)
    print(math.floor(factDigs) + 1)
    return 1 + math.floor(factDigs)


def calcExcls(enemyDigs, excls):
    if(enemyDigs > noDigits(excls)):
        loudness = ''
        for ex in range(0, excls):
            loudness += "!"
        return "IT'S OVER 9000" + loudness
    print("lol?")
    return calcExcls(enemyDigs, excls+1)


def yell(enemyDigs):
    if(enemyDigs < 1):
        return "..."
    if(enemyDigs > 31682):
        return "IT'S OVER 9000!"

    return calcExcls(enemyDigs, 1)


for i in range(0, len(arr)):
    shout = yell(int(arr[i][0]))
    print("Case #{}: ".format(i+1) + shout)
