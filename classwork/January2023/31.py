# def f(x, a1, a2):
#     return ((a1<=x<=a2)<= (430<=x<=490)) or (440<= x<= 530)

# m = 0
# for a1 in range(400,600):
#     for a2 in range(a1+1, 600):
#         if all(f(x, a1, a2) == 1 for x in range(400,600)):
#             m = max(m, a2 - a1)
# print(m/10) ответ 10



# def f(x, a1, a2):
#     return ((a1<=x<=a2)<= (150<=x<=390)) or (440<= x<= 570)

# m = 0
# for a1 in range(100,600):
#     for a2 in range(a1+1, 600):
#         if all(f(x, a1, a2) == 1 for x in range(100,600)):
#             m = max(m, a2 - a1)
# print(m/10) ответ 24



# def f(x, a1, a2):
#     return ((150<=x<=390)<=(a1<=x<=a2))and((440<=x<=570)<=(a1<=x<=a2))

# m = 99999999999999999999999999999999999999
# for a1 in range(100,600):
#     for a2 in range(a1+1, 600):
#         if all(f(x, a1, a2) == 1 for x in range(100,600)):
#             m = min(m, a2 - a1)
# print(m/10) ответ 42
