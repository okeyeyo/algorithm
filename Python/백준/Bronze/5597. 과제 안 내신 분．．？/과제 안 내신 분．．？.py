student_n = []
s_submit = []
n_submit = []

for i in range(30) :
  student_n.append(i+1)

for i in range(28) :
  s_submit.append(int(input()))

for i in student_n :
  if i not in s_submit :
    n_submit.append(i)

sorted_n_submit = sorted(n_submit)

for i in range(2) :
  print(sorted_n_submit[i])
