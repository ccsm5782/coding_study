n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
now = 99 * 100

# (흰, 검)
arr = [[-1] for _ in range((99 * 1000) * 2 + 1)]
# print(arr)
# print(len(arr))
for num, direction in commands:
    if direction == 'L':
        for i in range(int(num)):
            arr[now-i].append(1)
        now -= (int(num) - 1)
    else:
        for i in range(int(num)):
            arr[now+i].append(0)
        now += (int(num) - 1)

# print(arr[9895:9910])

black, grey, white = 0, 0, 0

for i in range((99 * 1000) * 2 + 1):
    if arr[i].count(1) >= 2 and arr[i].count(0) >= 2:
        grey += 1
    elif arr[i][-1] == 1:
        white += 1
    elif arr[i][-1] == 0:
        black += 1


print(white, black, grey)