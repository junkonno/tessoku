#関数定義
def search(x, A):
  L = 0
  R = N-1

  while L<=R:
    M = (L+R)//2
    if A[M] < x:
      L = M + 1
    elif A[M] == x:
      return M
    elif A[M] > x:
      R = M - 1
  return -1

#入力受取
N,X =map(int, input().split())
A = list(map(int, input().split()))

Answer = search(X,A)
print(Answer + 1)
