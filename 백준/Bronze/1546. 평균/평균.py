N = int(input())
score = list(map(int, input().split()))
M = max(score)
avg = 0.0
result = 0.0

for i in range(N) :
  mean = score[i]/M*100
  avg += mean
  result = avg/N

print(result)