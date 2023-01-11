def f(x, a):
    return ( x % a != 0 and x % 21 == 0) <= (x % 14 != 0)

for a in range(1, 10000):
    ok = True
    for x in range(1, 10000):
        if not f(x, a):
            ok = False
            break
    if ok:
        print(a)