a = [int(x) for x in open('17.txt')]
min6 = 10001
for i in range(len(a)):
    if abs(a[i]) % 10 == 6:
        min6 = min(min6, a[i])
ans=[]
for i in range(len(a)-1):
    if (abs(a[i]) % 10 == 6) or (abs(a[i + 1]) % 10 != 6) and abs((a[i]**2+a[i + 1]**2)) :
        ans.append(a[i]**2+a[i + 1]**2)
print(len(ans), max(ans))
