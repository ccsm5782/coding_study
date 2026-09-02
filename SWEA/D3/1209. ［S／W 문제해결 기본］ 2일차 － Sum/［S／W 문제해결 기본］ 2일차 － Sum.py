for i in range (10): # 테스트케이스는 10개
    t = int(input())
    arr = []
    for j in range(100):
        arr.append(list(map(int,input().split())))

    value = 0 # 구하려는 최대

    for j in range(100): # 가로 방향 탐색
        s = 0
        for k in range(100):
            s += arr[j][k]
        if s > value:
            value = s

    for j in range(100): # 세로 방향 탐색
        s = 0
        for k in range(100):
            s += arr[k][j]
        if s > value:
            value = s

    s = 0 # 왼쪽 위부터 오른쪽 아래 대각선
    for j in range(100):
        for k in range(100):
            if j == k:
                s += arr[j][k]
    if s > value:
        value = s

    s = 0 # 오른쪽 위부터 왼쪽 아래 대각선
    for j in range (100):
        s += arr[j][99-j]
    if s > value:
        value = s

    print(f"#{i+1} {value}")