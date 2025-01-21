import bisect

#入力受取
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]
A.sort()

#各Qに対して回答する
for i in range(Q):
  index = bisect.bisect_left(A, X[i])
  print(index)
