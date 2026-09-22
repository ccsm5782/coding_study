n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
arr = [[0] for _ in range(100*99*2 + 1)]
# print(len(arr))

now = 100*99

for num, direction in commands:
    if direction == 'R': # 오른쪽 검은색
        for i in range(int(num)):
            arr[now + i].append(1)
        now = now + int(num) - 1
    else:
        for i in range(int(num)):
            arr[now - i].append(-1)
        now = now - int(num) + 1

white, black = 0, 0

for i in range(100*99*2 + 1):
    if arr[i][-1] == 1:
        black += 1
    if arr[i][-1] == -1:
        white += 1

print(white, black) 