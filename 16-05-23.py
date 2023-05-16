# def f(s,c,m):
#     if s >= 43: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s+1,c+1,m),f(s+2,c+1,m),f(s*2,c+1,m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h) # any(f) в конце для номера 15
#
# for s in range(1, 43):
#     for m in range(1,5):
#         if f(s,0,m) == 1:
#             print(s,m)

# count = 0
# for x in range(1, 9):
#     for y in range(1, 7):
#         count += 1
# print(count)

# maxx = 0
# for i in range(99):
#     s = '1' * i
#     while ('1111' in s):
#         s = s.replace('1111', '22', 1)
#         s = s.replace('222', '1', 1)
#     if maxx < s.count('1'):
#         maxx = s.count('1')
#         index = i
# print(index)

# c = 0
# for i in range(500000, 600000):
#     for d in range(18, (i//2 + 1)):
#         if ((i % d) == 0) and ((d % 10) == 8):
#             c += 1
#             print(i, d)
#             break
#     if c == 5:
#         break

# def f(d):
#     if d[2] == [0]:
#         return d[1]
#     else:
#         maxx = 0
#         for i in d[2]:
#             if maxx < f(index[i - 1]):
#                 maxx = f(index[i - 1])
#         return maxx + d[1]
#
#
# from csv import reader
#
# with open("22_7.csv") as F:
#     s = reader(F, delimiter=';', quotechar='"')
#     next(s)
#     index = []
#     for i in s:
#         index.append([int(i[0]), int(i[1]), list(map(int, str(i[2]).split(';')))])
#     for i in range(len(index)):
#         print(i + 1, f(index[i]))

# def f(x, h):
#     if h == 3 and x >= 35:
#         return 1
#     elif h == 3 and x < 35:
#         return 0
#     elif x >= 35 and h < 3:
#         return 0
#     else:
#         if h % 2 == 0:
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)
#         else:
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)
#
#
# for x in range(1, 35):
#     if f(x, 1) == 1:
#         print("Задача 19: ", x)
#         break
#
# # ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# def f(x, h):
#     if h == 4 and x >= 35:
#         return 1
#     elif h == 4 and x < 35:
#         return 0
#     elif x >= 35 and h < 4:
#         return 0
#     else:
#         if h % 2 != 0:
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)  # стратегия победителя
#         else:
#             return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)  # стратегия проигравшего
#
#
# for x in range(1, 35):
#     if f(x, 1) == 1:
#         print("Задача 20: ", x)
# #.................................................................
# def f(x, h):
#     if (h == 3 or h == 5) and x >= 35:
#         return 1
#     elif h == 5 and x < 35:
#         return 0
#     elif x >= 35 and h < 5:
#         return 0
#     else:
#         if h % 2 == 0:
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)  # стратегия победителя
#         else:
#             return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)  # стратегия проигравшего
#
#
# def f1(x, h):
#     if h == 3 and x >= 35:
#         return 1
#     elif h == 3 and x < 35:
#         return 0
#     elif x >= 35 and h < 3:
#         return 0
#     else:
#         if h % 2 == 0:
#             return f1(x + 1, h + 1) or f1(x + 2, h + 1) or f1(x * 2, h + 1)  # стратегия победителя
#         else:
#             return f1(x + 1, h + 1) and f1(x + 2, h + 1) and f1(x * 2, h + 1)  # стратегия проигравшего(любой ход)
#
#
# for x in range(1, 35):
#     if f(x, 1) == 1:
#         print(x)
# print("====")
# for x in range(1, 35):
#     if f1(x, 1) == 1:
#         print(x)


# with open('17.txt') as f:
#     s = [int(x)for x in f]
#     res = []
#     for i in range (0, len(s)):
#         for j in range(i+1, len(s)):
#             if ((s[i]-s[j]) % 60 == 0) and (((s[i]) % 15 == 0) or ((s[j]) % 15 == 0)):
#                 res.append(s[i]-s[j])
# print(len(res), max(res))

# count = m = 0
# f = open('17.txt')
# l = [int(i) for i in f]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] % 5 == 0:
#             count += 1
#             m = max(m, l[i] + l[j])
# print(count, m)


# def f(x, y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 1, y) + f(x + 3, y)
# print(f(17, 30))


# f=open(r'24.txt')
# s=f.read()
# count=0
# max_count=0
# i=0
# while i < len(s):
#     if (s[i]=='C' or s[i]=='D' or s[i]=='F') and (s[i+1]=='A' or s[i+1]=='O'):
#         count+=1
#         i+=2
#         if max_count < count:
#             max_count=count
#     else:
#         count=0
#         i+=1
# print(max_count)

'''============================================================================================'''
# count = m = 0
# f = open('17.txt')
# l = [int(i) for i in f]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] + l[j]) % 2 != 0 and (l[i] * l[j]) % 5 == 0:
#             count += 1
#             m = max(m, l[i] + l[j])
# print(count, m)
'''============================================================================================'''
import math
i = int(math.sqrt(123456789))+1
j=i*i
while j <= 223456789:
    n = 0
    d = 0
    for k in range(2,i):
        if j%k == 0:
            n = n+1
            d = j//k
            if n>1: break
    if n == 1:
        print(j,d)
    i = i+1
    j = i*i

'''============================================================================================'''
# f = open(’26.txt’)
# n = int(f.readline())
# a = []
# for i in range(n):
#     x, y = [int(_) for _ in f.readline().split()]
#     a.append([x, y])
# a.sort()
#
# ans = [0, 0]
#
# for i in range(n - 1):
#     if a[i][0] == a[i + 1][0] and a[i][1] == a[i + 1][1] - 3:
#         row = a[i][0]
#         seat = a[i][1] + 1
#         if row > ans[0]:
#             ans[0] = row
#             ans[1] = seat
#
# print(*ans)

f = open('26.txt')
n = int(f.readline())
nums = []
for _ in range(n):
    pair = list(map(int, f.readline().split()))
    pair[1] = -pair[1]
    nums += [pair]
nums.sort()
r, m = 0, 0
for i in range(1, len(nums)):
    if nums[i][0] == nums[i-1][0]:
        if nums[i][1] - nums[i-1][1] == 3:
            r = nums[i][0]
            m = -nums[i][1] + 1
print(r, m)

f = open('26(1).txt')
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i] % 2 == 0 and n[j] % 2 == 0:
            s = (n[i] + n[j]) // 2
            if s in ns:
                c += 1
                if s > m:
                    m = s
print(c, m)










'''==========================================================================================='''
