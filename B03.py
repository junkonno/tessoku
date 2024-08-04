N = int(input())
l = list(map(int, input().split()))

hantei = False

for x in range(N):
  for y in range(x+1, N):
    for z in range(y+1, N):
      if l[x] + l[y] + l[z] == 1000:
        hantei = True

if hantei == True:
  print("Yes")
else:
  print("No")