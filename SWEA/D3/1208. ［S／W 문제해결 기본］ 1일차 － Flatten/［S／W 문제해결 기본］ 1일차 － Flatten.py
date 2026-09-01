for T in range(10): # T: 테스트 케이스
    d = int(input()) # d: 덤프 가능 횟수
    arr = list(map(int, input().split())) # arr: 이번 박스 모양
    max_min = 0 # max_min: 최대 - 최소
    max_idx = 0 # 최대 자리 idx
    min_idx = 0 # 최소 자리 idx

    # d 번의 반복
    for i in range(d):

        # max, min idx 번호 찾기
        for j in range(100):

            if arr[max_idx] < arr[j]:
                max_idx = j

            if arr[min_idx] > arr[j]:
                min_idx = j

        # 만약 차이가 0 또는 1이면 break
        if arr[max_idx] - arr[min_idx] == 0:
            max_min = 0
            break
        if arr[max_idx] - arr[min_idx] == 1:
            max_min = 1
            break

        # 차이가 0 또는 1이 아니라면 하나씩 옮기기
        arr[max_idx] -= 1
        arr[min_idx] += 1

        # 이때 정답 -> 근데 여기서 min 자리나 max 자리가 바뀔 수 있음
        max_min = max(arr) - min(arr)

    print(f"#{T+1} {max_min}")