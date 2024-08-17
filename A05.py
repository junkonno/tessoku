N, K = map(int, input().split())

count = 0

for x in range(1, N+1):
  for y in range(1, N+1):
    if K - x - y >= 1 and K - x - y < N+1:
      count+=1

print(count)
