# N, X, Y = input().split()

# for a in range(int(N)):
#     a += 1
#     if int(a) % int(X) == 0 and int(a) % int(Y) == 0:
#         print("AB")
#     elif int(a) % int(X) == 0:
#         print("A")
#     elif int(a) % int(Y) == 0:
#         print("B")
#     else:
#         print("N")

# N, K = [int(x) for x in input().split()]
# print(N)
# print(K)

# S = input()
# def test(a):
#     b = "aiueoAIUEO"
#     return "".join(c for c in a if c not in b)

# print(test(S))

# for num in range(1,1001):
#     print(num)

# import random
# num = random.randint(1,100)
# print(num)

# import datetime

# a = datetime.date.today()
# print(a)1

# import random
# list = input().split(" ")
# count = len(list)
# attack = random.randrange(count)

# print("{}に会心の一撃! {}を倒した".format(list[attack], list[attack]))
# a = input()
# z = []
# for b in a:
#     if b == "A":
#         c = 4
#         z.append(c)
#     elif b == "E":
#         c = 3
#         z.append(c)
#     elif b == "G":
#         c = 6
#         z.append(c)
#     elif b == "I":
#         c = 1
#         z.append(c)
#     elif b == "O":
#         c = 0
#         z.append(c)
#     elif b == "S":
#         c = 5
#         z.append(c)
#     elif b == "Z":
#         c = 2
#         z.append(c)

# print(z)

# a, count = input().split(" ")
# money = int(a)
# point = 0

# for i in range(int(count)):
#     cost = int(input())
#     if point > cost:
#         point -= cost
#         print(money, point)
#     else:
#         money -= cost
#         point += cost // 10
#         print(money, point)

# count, line = input().split()

# for i in range(int(count)):
#     score, absence = input().split()
#     final_score = int(score) - int(absence) * 5
#     if int(line) <= final_score:
#         print(i + 1)

# time = input().split(":")
# hour = int(time[0])
# minutes = int(time[1]) + 30

# if minutes > 60:
#     minutes -= 60
#     hour += 1
#     if hour < 10:
#         hour_zero = "0" + str(hour)
#         print(str(hour_zero) + ":" + str(minutes))
#     else:
#         print(str(hour) + ":" + str(minutes))
# elif hour < 10:
#     hour_zero = "0" + str(hour)
#     print(str(hour_zero) + ":" + str(minutes))
# else:
#     print(str(hour) + ":" + str(minutes))

# S = input()
# h = int(S[:2])
# m = int(S[3:])

# if m + 30 >= 60:
#     h = str(h + 1)
#     m = str(m + 30 - 60)
# else:
#     h = str(h)
#     m = str(m + 30)

# if len(h) == 1:
#     h = "0" + h
# if len(m) == 1:
#     m = "0" + m

# print(h + ":" + m)

# count = int(input())
# list = []

# for i in range(count):
#     time = input().split(" ")
#     list.append(time)
# for time in list:
#     h = time[1]
#     m = time[2]
#     start = time[0].split(":")
    
#     finish_m = int(start[1]) + int(m)
#     if finish_m > 60:
#         finish_m -= 0
#         finish_h += 1
#         if finish_m < 10:
#             finish_m = "0" + str(finish_m)
#     elif finish_m < 10:
#         finish_m = "0" + str(finish_m)
    
#     finish_h = int(start[0]) + int(h)
#     if finish_h > 24:
#         finish_h -= 24
#         if finish_h < 10:
#             finish_h = "0" + str(finish_h)
#     elif finish_h < 10:
#         finish_h = "0" + str(finish_h)
#     print(str(finish_h) + ":" + str(finish_m))
    
# N = int(input())

# for i in range(N):
#     [t, h, m] = input().split()
#     th = int(t[:2])
#     tm = int(t[3:])
#     h = int(h)
#     m = int(m)

#     ah = th + h
#     am = tm + m

#     if am >= 60:
#         ah += 1
#         am -= 60
#     if ah >= 24:
#         ah -= 24

#     ah = str(ah)
#     am = str(am)

#     if len(ah) == 1:
#         ah = "0" + ah
#     if len(am) == 1:
#         am = "0" + am

#     print(ah + ":" + am)

# count, size = input().split()
# size = int(size) * 2
# list = []

# for i in range(int(count)):
#     a = input().split()
#     list.append(a)

# for (i, j) in enumerate(list):
#     if int(size) <= int(j[0]) and int(size) <= int(j[1]) and int(size) <= int(j[2]):
#         print(i + 1)

# count = int(input())
# key = input()
# list = []

# for i in range (count):
#     word = input()
#     list.append(word)

# for j in list:
#     if key in j:
#       print(j)
#     else:
#       print("None")