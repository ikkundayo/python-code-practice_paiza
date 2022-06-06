# ①Fizz Buzz (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/skillcheck_sample/fizz-buzz?language_uid=python3

# a = int(input())

# for b in range(a):
#     b += 1

#     if b % 15 == 0:
#         print("Fizz Buzz")
#     elif b % 3 == 0:
#         print("Fizz")
#     elif b % 5 == 0:
#         print("Buzz")
#     else:
#         print(b)


# ②単語のカウント (paizaランク C 相当)
# url: none

# a = input().split()
# dic = {}

# for b in a:
#     if b in dic:
#         dic[b] += 1
#     else:
#         dic[b] = 1

# for key, value in dic.items():
#     print(key, value)


# ③検索履歴 (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/skillcheck_archive/search_history?language_uid=python3

# num = int(input())

# words = []

# for _ in range(num):
#     input_word = input()
#     words.append(input_word)

# for word in reversed(words):
#     print(word)


# ④宝くじ (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/skillcheck_archive/lottery?language_uid=python3

# win_num = int(input("number"))
# buy_num = int(input("how much?"))

# lotteries_number_list = []

# for _ in range(buy_num):
#     lotteries_number_list.append(int(input()))

# for lot_num in lotteries_number_list:
#     if lot_num == win_num:
#         print("一等")
#     elif win_num - 1 <= lot_num <= win_num + 1:
#         print("前後賞")
#     elif str(lot_num)[2:] == str(win_num)[2:]:
#         print("２等")
#     elif str(lot_num)[3:] == str(win_num)[3:]:
#         print("3等")
#     else:
#         print("ハズレ")


# ⑤野球の審判 (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/skillcheck_archive/umpire?language_uid=python3

# num = int(input("総球数"))
# results = {"strike":0, "ball":0}

# for _ in range(num):
#     judge = input("判定")
#     results[judge] += 1

#     if results["strike"] == 3:
#         print("Out!")
#     elif results["ball"] == 4:
#         print("fourball!")
#     else:
#         print(judge + "!")


# ⑥西暦の和暦変換 (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/dateset/ad_to_era?language_uid=python3

# year, month, day = input().split()

# new_month = month
# new_day = day

# if int(month) < 10:
#     new_month = "0" + month
# if int(day) < 10:
#     new_day = "0" + day

# date = int(year + new_month + new_day)

# if date >= 20190501:
#     print("令和年{}月{}日".format(month, day))
# elif date >= 19890108:
#     print("平成年{}月{}日".format(month, day))
# elif date >= 19261225:
#     print("昭和年{}月{}日".format(month, day))
# elif date >= 19120730:
#     print("大正年{}月{}日".format(month, day))
# else:
#     print("明治年{}月{}日".format(month, day))


# ⑦西暦の和暦変換2 (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/dateset/ad_to_era2?language_uid=python3

# year, month, day = input().split()

# new_month = month
# new_day = day

# if int(month) < 10:
#     new_month = "0" + month
# if int(day) < 10:
#     new_day = "0" + day

# date = int(year + new_month + new_day)

# def first_year(year):
#     if year == 1:
#         year = "元"
#     return year

# if date >= 20190501:
#     year = first_year(int(year) - 2018)
#     print("令和{}年{}月{}日".format(year, month, day))
# elif date >= 19890108:
#     year = first_year(int(year) - 1988)
#     print("平成{}年{}月{}日".format(year, month, day))
# elif date >= 19261225:
#     year = first_year(int(year) - 1925)
#     print("昭和{}年{}月{}日".format(year, month, day))
# elif date >= 19120730:
#     year = first_year(int(year) - 1911)
#     print("大正{}年{}月{}日".format(year, month, day))
# else:
#     year = first_year(int(year) - 1867)
#     print("明治{}年{}月{}日".format(year, month, day))


# ⑧月の日数 (paizaランク C 相当)
# url: https://paiza.jp/works/mondai/dateset/days_in_a_month?language_uid=python3

# year, month = [int(x) for x in input().split()]

# month_list = [4, 6, 9, 11]

# if month in month_list:
#     print(30)

# elif month == 2:
#     if year % 100 == 0:
#         print(29)
#     elif year % 400 == 0:
#         print(28)
#     elif year % 4 == 0:
#         print(29)
#     else:
#         print(28)

# else:
#     print(31)