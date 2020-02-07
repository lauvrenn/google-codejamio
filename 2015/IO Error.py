import sys
lines = int(input())
arr = []

for i in range(0, lines * 2):
    n = [s for s in input().split("\n")]
    arr.append(n)

m = 0
for i in range(0, len(arr), 2):
    arr[i+1][0] = arr[i+1][0].replace("I", "1")
    arr[i+1][0] = arr[i+1][0].replace("O", "0")

    case = ''
    for k in range(0, int(arr[i][0])):
        eight = arr[i+1][0][k*8+1:k*8+8]
        case += chr(int(eight, 2))
    m += 1
    print("Case #{}: ".format(m) + case)

# TEST CASES
# 2
# 2
# OIOOIIIIOIOOIOII
# 21
# OIOOIOOIOOIOOOOOOOIOOIIIOOIIIIOOOOIIOOIIOOIOOIIIOOIOOOOOOOIOOOIOOIOOOOIIOOIIOOOOOIIOOIOOOOIIOOIIOOIOOOOOOIOOIOIOOOIIOIOOOIIOIIOIOOIOOOIOOOIOOOOIOOIOOOOOOOIIIOIOOOIOIOOI
