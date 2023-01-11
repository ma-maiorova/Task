def f(a, b):
    # a, b = числа из условия в виде строк
    size = max(len(a), len(b))
    a = '0' * (size - len(a)) + a
    b = '0' * (size - len(b)) + b
    c = [0 for i in range(size)]
    p = 0
    for i in range(size - 1, -1, -1):
        c[i] = int(a[i]) + int(b[i]) + p
        p = c[i] // 10
        c[i] %= 10
    if p != 0:
        c = [p] + c
    ans = ''
    for i in c:
        ans += str(i)
    return ans

a = input()
b = input()
print(f(a, b))