lines = int(input())
arr = []

for i in range(1, lines + 1):
    n = [s for s in input().split("\n")]
    arr.append(n)


def dashes(strlength):
    line = '+'
    for dashes in range(1, strlength + 3):
        line = line + '-'
    line = line + '+'
    return line


def generateBox(text):
    result = ''
    strlength = len(text)
    result += dashes(strlength) + '\n'

    line = ''
    line = '| ' + text + ' |'
    result += line + '\n'

    line = dashes(strlength)
    result += line

    return result


for cases in range(1, len(arr) + 1):

    print("Case #{}:".format(cases))

    result = generateBox(arr[cases-1][0])

    print(result)


### TEST CASES ###

# 5
# Merry Saturnalia, Giovanni!
# Equus, you're the best!
# Caballus, you try really hard!

# w
