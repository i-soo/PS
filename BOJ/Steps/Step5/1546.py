n = int(input())
score_list = list(map(int, input().split()))

m = max(score_list)

result = 0
for i in range(n):
    score_list[i] = score_list[i]/m*100
    result += score_list[i]
    
result /= n
print(result)
