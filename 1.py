def f(x):
    global p, q, a
    return (not x in p) or ((not x in q) <= (x in a))

p = set([2, 4, 6, 8, 10, 12])
q = set([3, 6, 9, 12, 15])
a = set()

for x in range(0, 100):
    if not f(x):
        a.add(x)

ans = 1
for i in a:
    ans *= i
print(ans)