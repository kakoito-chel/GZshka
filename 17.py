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
