T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    # print(arr)
    # print(visit)

    r, c = 0, 0
    delta = [[0,1], [1,0], [0,-1], [-1,0]]
    num = 1
    arr[r][c] = num
    visit[r][c] = 1

    while True:
        for move_r, move_c in delta:
            nr, nc = r + move_r, c + move_c
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                r = nr
                c = nc
                num += 1
                arr[r][c] = num
                visit[r][c] = 1
                break
        if num == N ** 2:
            break

    print(f"#{tc}")
    for line in arr:
        print(*line)