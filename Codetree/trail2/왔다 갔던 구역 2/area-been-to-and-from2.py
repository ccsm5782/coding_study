n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

answer = [0]*2001
now = 1000
# Please write your code here.
for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            answer[now - 1 - j] += 1
        now -= x[i]
    else:
        for j in range(x[i]):
            answer[now + j] += 1
        now += x[i]

cnt = 0
for _ in range(2001):
    if answer[_] >= 2:
        cnt += 1

print(cnt)

