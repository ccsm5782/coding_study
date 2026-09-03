TC = int(input())

for i in range(TC):
    N = int(input())
    arr = list(map(int, input().split()))

    # 선택정렬
    for j in range(N):
        max_idx = 0
        for k in range(N-j):
            if arr[max_idx] < arr[k]:
                max_idx = k
        arr[max_idx], arr[N-1-j] = arr[N-1-j], arr[max_idx]

    # 정렬한 수열을 담을 공간
    answer = []

    if N % 2 == 1: # 홀수개의 숫자라면
        for j in range(N//2):
            answer.append(arr[N-j-1])
            answer.append(arr[j])
        answer.append(arr[N//2 + 1])

    else: # 짝수개의 숫자라면
        for j in range(N//2):
            answer.append(arr[N-j-1])
            answer.append(arr[j])

    print(f"#{i+1}", end= ' ')
    for i in range(10):
        print(answer[i], end=' ')
    print()
