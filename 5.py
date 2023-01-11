f = open('k8-0.txt')
s = f.readline()

pr = s[0]
size = 1
mx = 0
ans = []

for i in range(1, len(s)):
    if (s[i] == pr):
        size += 1
    else:
        if size > mx:
            mx = size
            ans = [[pr, size]]
        elif size == mx:
            ans.append([pr, size])
        pr = s[i]
        size = 1

if size > mx:
    mx = size
    ans = [[pr, size]]
elif size == mx:
    ans.append([pr, size])

for i in ans:
    print(*i, end = ' ')