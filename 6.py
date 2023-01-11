ans = [0, 1000, 1000]
for x in range(1, 21 + 1):
    for y in range(12 + 1):
        o1 = 22
        o2 = 13
        a = x * o1 ** 4 + 2 * o1 ** 3 + 3 * o1 ** 2 + x * o1 + 5
        b = 6 * o2 ** 4 + 7 * o2 ** 3 + y * o2 ** 2 + 9 * o2 + y
        c = a - b
        if (c % 57 == 0):
            #print(x, y)
            if ans[1] + ans[2] > x + y:
                ans = [c // 57, x, y]

print(ans[0])
#print(ans)