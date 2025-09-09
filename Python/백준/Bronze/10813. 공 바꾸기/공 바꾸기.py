n, m = map(int, input().split())
basket = []
ano = [0]
for i in range(n) :
  basket.append(i+1)

for i in range(m) :
  i, j = map(int, input().split())
  ano[0] = basket[i-1]
  basket[i-1] = basket[j-1]
  basket[j-1] = ano[0]

result = ' '.join(map(str, basket))
print(result)