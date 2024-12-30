#入力受取
N = int(input())
A = list(map(int, input().split()))
D = int(input())
lr = [map(int, input().split()) for _ in range(D)]
l, r = [list(i) for i in zip(*lr)]

Al = [0] * (N+1)
Ar = [0] * (N+1)

#右からの最大値を取る
for i in range(N):
  if Al[i] < A[i]:
    Al[i+1] = A[i]
  else:
    Al[i+1] = Al[i]

#左からの最大値を取る
A.reverse()
for i in range(N):
  if Ar[i] < A[i]:
    Ar[i+1] = A[i]
  else:
    Ar[i+1] = Ar[i]

#Dに対してそれぞれの最大値を取る
for i in range(D):
  if Al[l[i]-1] > Ar[N-r[i]]:
    print(Al[l[i]-1])
  elif Al[l[i]-1] < Ar[N-r[i]]:
    print(Ar[N-r[i]])
  else:
    print(Al[l[i]-1])
