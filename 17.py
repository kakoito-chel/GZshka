a = [int(x) for x in open("17(2).txt")]
# ans = []
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if (a[i]*a[j]) % 34 != 0:
#             ans.append(a[i]+a[j])
# print(len(ans), max(ans))

s = 0
mx = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] % 160 != a[j] % 160) and ((a[i] % 7 == 0) or (a[j] % 7 == 0)):
            s += 1
            mx = max(mx, a[i] + a[j])
print(s, mx)

f = open('24.txt').readline()
k = 1
m = 0
for i in range(1, len(f)):
    if f[i] != f[i-1]:
        k += 1
    else:
        m = max(m, k)
        k = 1
m = max(m, k)
print(m)

f=open('24_demo.txt')
s=f.readline()
mx=1
cnt=1
for i in range(len(s)-1):
    if s[i]=='X' and s[i+1]=='X':
        cnt+=1
        if cnt>mx:
            mx=cnt
    else:
        cnt=1
mx = max(cnt, mx)
print(mx)

f = open('24.txt').readline()
k = mx = 0
for i in range(len(f)):
    if f[i-1:i+1] in 'XYZX' and k:
        k += 1
    elif f[i] == 'X':
        k = 1
    else:
        k = 0
    mx = max(mx, k)
print(mx)
