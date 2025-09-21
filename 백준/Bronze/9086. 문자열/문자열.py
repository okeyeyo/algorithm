num = int(input())
str = []
length = []
for i in range(num) :
  str.append(list(input()))

for i in range(num) :
  print(str[i][0]+str[i][-1])
