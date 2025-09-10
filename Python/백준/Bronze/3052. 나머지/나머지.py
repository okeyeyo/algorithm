num = [0] * 10
mod = []

for i in range(10) :
  num[i] = int(input())

for i in num :
  mod.append(i % 42)

cnt = len(set(mod)) # 중복을 허용하지 않는 순서가 없는 집합이다.
print(cnt)