lines = int(input().strip())
arr = []

for i in range(0, lines):
    input().strip()
    o = [int(s) for s in input().split(" ")]
    arr.append(o)


def error(val):
    er = 0
    K = len(val)
    for i in range(0, K):
        disend = K - i - 1
        minim = -1
        if(disend < i):
            minim = disend
        else:
            minim = i
        er += (val[i]-minim)**2
    return er


def calc(ingr):
    num = len(ingr)
    newone = [-1]*num
    loo = num
    if num % 2 != 0 or num == 1:
        loo += 1
    for i in reversed(range(0, int(loo/2))):
        if len(ingr) != 0:
            maxx = max(ingr)
            newone[i] = maxx
            ingr.remove(maxx)
        if len(ingr) != 0 and num-i-1 != i:
            maxx = max(ingr)
            newone[num-i-1] = maxx
            ingr.remove(maxx)
    return error(newone)


for i in range(0, lines):
    final = calc(arr[i])
    print("Case #{}: ".format(i+1) + str(final))
