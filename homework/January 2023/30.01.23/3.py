P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
A = set(range(1,8192))

def f(x):
  return ((x in A) <= (x in P)) or ((not(x in Q)) <= (not(x in A)))


for x in range(-8192, 8192):
  if f(x) == 0:
    A.remove(x)

print(A, len(A)) # 18 (количество)
