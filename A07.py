D = int(input())
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
B = [0] * (D + 2)
A = [0] * (D + 2)

for i in range(N):
  B[l[i][0]] += 1
  B[l[i][1]+1] -= 1

for i in range(1, D+1):
  A[i] = A[i-1] + B[i]

for i in range(1, D+1):
  print(A[i])