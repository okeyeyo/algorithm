n, m = map(int, input().split())
basket = [0] * n
for i in range(m) :
  i,j,k = map(int,input().split())
  for arr in range(i-1, j) :
    basket[arr] = k

re = ' '.join(map(str, basket))
print(re)