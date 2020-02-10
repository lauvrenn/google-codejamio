lines = int(input().strip())
arr = []

for i in range(0, lines):
    n = [int(s) for s in input().split("\n")]
    o = [int(s) for s in input().split(" ")]
    n.append(o)
    arr.append(n)


def calc(case):
    prices = case[1]
    sale = []
    for k in reversed(range(0, int(case[0]))):
        maxpr = max(prices)
        salepr = int(int(maxpr)*0.75)
        if(salepr in prices):
            prices.remove(maxpr)
            prices.remove(salepr)
            sale.append(salepr)
    sale.sort()
    return sale


for i in range(0, lines):
    res = calc(arr[i])
    print("Case #{}: ".format(i+1) + str(' '.join(map(str, res))))

# 1
# 3
# 15 20 60 75 80 100
