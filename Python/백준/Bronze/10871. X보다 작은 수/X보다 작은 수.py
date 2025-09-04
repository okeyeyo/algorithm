num = list(map(int, input().split()))
arr = list(map(int, input().split()))
sm = []

for i in range(len(arr)) :
  if arr[i] < num[1] :
    sm.append(arr[i])
re = ' '.join(map(str, sm)) # join은 문자열들을 연결해서 하나의 문자열로 만드는 메서드이므로 숫자나 다른 타입이 있으면 안됨
print(re)