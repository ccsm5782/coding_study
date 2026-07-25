Test_case = int(input())

for _ in range(Test_case):
    N, S = input().split() # S는 문자열
    n = int(N) # n은 문자열의 길이
    table = {(0,0): 1}
    pa, pc = 0, 0
    count = 0
    
    for ch in S:
        if ch == 'A':
            pa += 1
        elif ch =='T':
            pa -= 1
        elif ch =='C':
            pc += 1
        elif ch =='G':
            pc -= 1
            
        key = (pa, pc)
        count = count + table.get(key, 0)
        table[key] = table.get(key, 0) + 1
        
    print(count)
             
            
            

    