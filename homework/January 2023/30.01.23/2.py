P = {2, 4, 6, 8, 10, 12}
Q = {4, 8, 12, 116}
A = set()

def f(x):
  return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))


for x in range(-8192, 8192):
  if f(x) == 0:
    A.add(x)

print(A, sum(A)) # 24 (сумма)
