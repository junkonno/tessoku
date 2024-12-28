#初期化
#XYの取得
H,W,N = map(int, input().split())

#ABCDの取得
A = [ None ] * N
B = [ None ] * N
C = [ None ] * N
D = [ None ] * N

for i in range(N):
	A[i], B[i], C[i], D[i] = map(int, input().split())

#空の2次元平面の作成
Z = [ [ 0 ] * (W + 2) for i in range(H + 2) ]

#点の描画
for i in range(N):
  Z[A[i]][B[i]] += 1
  Z[C[i]+1][D[i]+1] += 1
  Z[C[i]+1][B[i]] -= 1
  Z[A[i]][D[i]+1] -= 1

#回答用の2次元平面の作成
R = [ [ 0 ] * (W+1) for i in range(H+1) ]

for i in range(1, H+1):
  for j in range(1, W+1):
    R[i][j] = R[i][j-1] + Z[i][j]
 
for j in range(1, W+1):    
  for i in range(1, H+1):
    R[i][j] = R[i-1][j] + R[i][j]

for i in range(1, H+1):
  row = ""
  for j in range(1, W+1):
    row = row + str(R[i][j]) + " "
  print(row)