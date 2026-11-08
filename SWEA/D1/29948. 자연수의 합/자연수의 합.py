T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    now_sum = 0
    while True:
        if now_sum >= n:
            break
        now_sum += cnt
        cnt += 1
        if now_sum >= n:
            break
    print(f"#{tc} {cnt-1}")