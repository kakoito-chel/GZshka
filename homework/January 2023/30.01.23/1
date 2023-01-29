P = {2,4,6,8,10,12,14,16,18,20}
Q = {3,6,9,12,15,18,21,24,27,30}
A = set()

def f(x):
   return ((x in P) <= (x in A)) or ((x not in A) <= (x not in Q))

for x in range(-8192, 8192):
  if f(x) == 0:
    A.add(x)

print(A) # 3 (количество)
