n, m = map(int, input().split())
N = [0] * n
temp = [0]
for i in range(n) :
  N[i] = i+1

for k in range(m) :
  i, j = map(int, input().split())
  N[i-1:j] = reversed(N[i-1:j])

result = ' '.join(map(str, N))
print(result)