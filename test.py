#①トリボナッチ数列生成関数
# def tribonacci_list(n, t0, t1, t2):
#     tri = [t0, t1, t2]
#     if n == 1:
#         tri = [t0]
#     elif n == 2:
#         tri = [t0, t1]
#     else:
#         for k in range(3, n):
#             tri.append(tri[k-1]+tri[k-2]+tri[k-3])
#     return tri

# # 1,1,2から始まる10項のトリボナッチ数列を生成
# tri = tribonacci_list(32, 1, 0, 5)

# print(tri[31])

# ②
# num = 1234567890
# divisors = []
# for i in range(1, num+1):
#     if num % i == 0:
#         divisors.append(i)
# print(divisors)

# list = [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90, 3607, 3803, 7214, 7606, 10821, 11409, 18035, 19015, 21642, 22818, 32463, 34227, 36070, 38030, 54105, 57045, 64926, 68454, 108210, 114090, 162315, 171135, 324630, 342270]
# sum_list = sum(list)
# print(sum_list)

# ③
# (ruby)

# sum = 0
# 1000000000000.times do |timesCount|
#   count = timesCount + 1
#   sum += 1.0/count
#   if sum >= 15
#    puts sum
#    puts count
#    return
#   end
# end

# ④
# a=range(1,30001)
# c=[]
# for i in a:
#     if (i%3==0) or ('3' in str(i)):
#         c.append(i)
# d = sum(c)
# print(d)
