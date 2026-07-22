n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    sum_a = a*(a+1) // 2
    sum_b = b*(b+1) // 2
    sum_c = c*(c+1) // 2    
    sum = sum_a * sum_b * sum_c
    print(sum % 998244353)
        
