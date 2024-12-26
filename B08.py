#初期化
#XYの取得
N = int(input())
X = [None] * (N)
Y = [None] * (N)

for i in range(N):
	X[i], Y[i] = map(int, input().split())

#ABCDの取得
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q

for i in range(Q):
	A[i], B[i], C[i], D[i] = map(int, input().split())
	
#空の2次元平面の作成
#1辺の最大値
max1 = 0
max2 = 0
max = 0
for i in range(Q):
  if max1 < C[i]:
    max1 = C[i]

for i in range(Q):
  if max2 < D[i]:
    max2 = D[i]
  
if max1 > max2:
  max = max1
elif max2 > max1:
  max = max2
else:
  max = max2

#空の2次元平面の作成
Z = [ [ 0 ] * (max + 1) for i in range(max + 1) ]

#XYの点を入れる
for i in range(N):
  Z[X[i]][Y[i]] += 1
  
#累積和を取る（Y軸, 1回目）
for i in range(1, max+1):
  for j in range(1, max+1):
    Z[i][j] = Z[i][j-1] + Z[i][j]

#累積和を取る（X軸, 2回目）
for j in range(1, max+1):
  for i in range(1, max+1):
    Z[i][j] = Z[i-1][j] + Z[i][j]

#最後に問題の計算
for i in range(Q):
	print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])