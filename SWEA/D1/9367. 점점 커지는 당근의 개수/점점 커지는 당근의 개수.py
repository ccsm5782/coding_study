T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 1
    cnt = 1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            cnt += 1
            if cnt > answer:
                answer = cnt
        else:
            cnt = 1
    print(f"#{testcase} {answer}")