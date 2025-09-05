n = []
for i in range(9) :
  n.append(int(input()))
big = max(n)
idx = n.index(big) + 1

print(big)
print(idx)
