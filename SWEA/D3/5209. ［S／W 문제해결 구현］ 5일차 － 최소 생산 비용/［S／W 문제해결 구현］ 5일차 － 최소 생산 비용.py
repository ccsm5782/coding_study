def dfs(cnt, n, score):
    global answer

    if cnt == n:
        if score < answer:
            answer = score
            return

    if score >= answer:
        return

    for i in range(n):
        if visit_col[i] == False:
            visit_col[i] = True
            dfs(cnt+1, n, score + arr[cnt][i])
            visit_col[i] = False

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = float('inf')
    visit_col = [False] * n
    dfs(0, n, 0)
    print(f"#{tc} {answer}")