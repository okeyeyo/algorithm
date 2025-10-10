data = list(input())
A = 65
P = 80
T = 84
time = 0

# 다이얼 값 조정
dial = [['0'] * 3 for _ in range(8)]
for i in range(0, 3, 2) :
  dial[i+5].append('0')

for i in range(5) :
  for j in range(3) :
    dial[i][j] = chr(A)
    A += 1
for i in range(0,3,2) :
  for j in range(4) :
    dial[i+5][j] = chr(P)
    P += 1
  P += 3
for i in range(3) :
  dial[6][i] = chr(T)
  T += 1

for char in data : # data의 각 문자
  for i in range(len(dial)) : # dial의 각 행
    if char in dial[i] : # data의 각 문자가 dial의 각 행에 존재하는지 확인
      time += i+3

print(time)