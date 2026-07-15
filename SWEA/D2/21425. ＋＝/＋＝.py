T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    '''count를 0이 아닌 1로 설정해야 하는 이유: 0으로 두면 안되는건 알겠는데 
    그렇다고 1로 이렇게 바로 둬도 되는지는 모르겠음
    '''
    count = 1     
    while a + b <= c:
        if a < b:
            a += b
            count += 1                        
        else:
            b += a
            count += 1            
    print(count)