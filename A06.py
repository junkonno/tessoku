N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [list(map(int, input().split())) for l in range(Q)]

for i in range(1, N):
  A[i] = A[i-1] + A[i]

A.insert(0, 0)

for x in range(Q):
  answer = A[L[x][1]] - A[L[x][0]-1]
  print(answer)
  
