T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maximum = max(arr)
    minimum = min(arr)
    print(f"#{i+1} {maximum - minimum}")
