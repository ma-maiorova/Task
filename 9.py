n, k = map(int, input().split())
a = list(map(int, input().split()))
ost = k
ans = 1
ok = True
for i in range(1, n):
    if (a[i] - a[i - 1] > k):
        ok = False
        break
    if (a[i] - a[i - 1] <= ost):
        ost -= a[i] - a[i - 1]
    else:
        ost = k
        ans += 1
if ok == False:
    ans = -1
print(ans)