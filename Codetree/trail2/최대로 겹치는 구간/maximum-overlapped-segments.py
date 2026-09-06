n = int(input()) # 테스트케이스
segments = [tuple(map(int, input().split())) for _ in range(n)] # [(어디부터, 어디까지), ...]

# Please write your code here.
arr = [0]*200
for a,b in segments:
    for i in range(a,b):
        arr[i] += 1

print(max(arr))