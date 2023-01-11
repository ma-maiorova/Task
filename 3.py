def f(ind):
    global a, ans, s
    if ind == 7:
        if a[0] != 'Я' and a.count('Я') == 1 and a.count('С') == 1:
            ans += 1
        return
    for i in s:
        a[ind] = i
        f(ind + 1)

s = 'САШУЛЯ'
a = [' ' for i in range(7)]
ans = 0
f(0)
print(ans)
