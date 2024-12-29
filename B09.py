#Nを取得
N = int(input())

#初期化
A = [ None ] * N
B = [ None ] * N
C = [ None ] * N
D = [ None ] * N

#座標を取得
for i in range(N):
	A[i], B[i], C[i], D[i] = map(int, input().split())

#空の配列
Z = [[ 0 ] * (1501) for i in range(1501)]

#累積和の下準備
for i in range(N):
  Z[A[i]][B[i]] += 1
  Z[C[i]][D[i]] += 1
  Z[C[i]][B[i]] -= 1
  Z[A[i]][D[i]] -= 1

#累積和 1軸目
for i in range(1501):
  for j in range(1, 1501):
    Z[i][j] = Z[i][j] + Z[i][j-1]

#累積和 2軸目
for j in range(1501):
  for i in range(1, 1501):
    Z[i][j] = Z[i][j] + Z[i-1][j]

# for i in range(0, 1501):
# 	for j in range(1, 1501):
# 		Z[i][j] = Z[i][j-1] + Z[i][j]

# for i in range(1, 1501):
# 	for j in range(0, 1501):
# 		Z[i][j] = Z[i-1][j] + Z[i][j]

#カウント
count = 0
for n in range(1501):
  for m in range(1501):
    if Z[n][m] > 0:
      count = count + 1

#出力
print(count)
