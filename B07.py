T = int(input())
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
B = [0] * (T + 2)
Answer = [0] * (T + 2)

for i in range(N):
  B[l[i][0]+1] += 1
  B[l[i][1]+1] -= 1
  
for i in range(1, T+1):
  Answer[i] = Answer[i-1] + B[i]

for i in range(1, T+1):
  print(Answer[i])
