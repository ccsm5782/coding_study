for tc in range (10):
    tn = int(input())
    arr = []

    # 첫 배치도 입력
    for i in range(100):
        arr.append(list(map(int, input().split())))

    # 배치도 뒤집기 (위 아래 방향)
    for j in range(50):
        arr[j], arr[99-j] = arr[99-j], arr[j]

    # 이동 내용 트래킹
    tracking = [[0] * 100 for _ in range(100)]

    # 첫 줄에서 2가 있는 위치 찾기
    idx = 0
    while arr[0][idx] != 2:
        idx += 1

    # 첫 좌표 d1: 세로 이동, d2: 가로 이동
    d1, d2 = 0, idx

    # 트래킹에 출발점 1로 표시
    tracking[d1][d2] = 1

    # 규칙 만들기
    # 0. 인덱스 범위가 초과하지 않는 선에서
    # 1. 양쪽에 길이 있으면 양 옆으로 이동
    # 2. 아래에 길이 있으면 아래로 이동

    # 양 옆 이동 정의: 오른쪽 이동, 왼쪽 이동, 아래 이동
    move = [[0, 1], [0, -1], [1, 0]]


    # 반복문
    # while True:
    #     if (0 <= d1 < 100) and (0 <= d2 < 100): # 인덱스 범위가 초과하지 않는다면
    #         for move_d1, move_d2 in move:
    #             if d2+move_d2 < 100 and arr[d2+move_d2] == 1: # 오른쪽으로 옮겨도 문제가 없다면
    #                 d2 = d2+move_d2 # d2 자리를 변경한다
    #                 break
    #             if d2 + move_d2 >= 0 and arr[d2 + move_d2] == 1:  # 왼쪽으로 옮겨도 문제가 없다면
    #                 d2 = d2 + move_d2  # d2 자리를 변경한다
    #                 break
    #             if d1 + move_d1 < 100 and arr[d1 + move_d1] == 1:  # 아래로 옮겨도 문제가 없다면
    #                 d1 = d1 + move_d1  # d1 자리를 변경한다
    #                 break
    #     else:
    #         break

    # 이대로 하니까 왔던 가로 길을 또 방문하는 문제가 생긱 됨. 이를 해결하기 위해 이동한 길을 남기는 코드를 작성

    while d1 != 99:
        for move_d1, move_d2 in move:
            if 0 <= d2+move_d2 < 100 and tracking[d1][d2+move_d2] == 0 and arr[d1][d2+move_d2] == 1:  # 인덱스 문제 없고, 방문하지 않았던 곳이고, 오른쪽으로 갈 수 있다면,
                d2 = d2+move_d2 # d2 자리를 변경한다
                tracking[d1][d2] = 1
                break
            if 0 <= d2+move_d2 < 100 and tracking[d1][d2+move_d2] == 0 and arr[d1][d2 + move_d2] == 1:  # 왼쪽
                d2 = d2 + move_d2  # d2 자리를 변경한다
                tracking[d1][d2] = 1
                break
            if d1+move_d1 < 100 and tracking[d1+move_d1][d2] == 0 and arr[d1 + move_d1][d2] == 1:  # 아래
                d1 = d1 + move_d1  # d1 자리를 변경한다
                tracking[d1][d2] = 1
                break


    print(f"#{tn} {d2}")