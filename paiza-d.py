# ①掛け算 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/skillcheck_sample/multiplication?language_uid=python3

# a = input("how are you?: ")
# print("あなたの今日の調子は",a,"ですね")

# a = int(input("好きな数字を入力してね!: "))
# b = a + 10
# print("あなたの結婚する年齢は", b, "です。")


# ②足し算 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/skillcheck_sample/addition?language_uid=python3

# a, b = input().split()
# print(int(a) + int(b))


# ③一番小さい値 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/skillcheck_sample/min_num?language_uid=python3

# list = []
# for _ in range(5):
#     list.append(int(input()))
# print(min(list))


# ④文字の一致 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/skillcheck_sample/diff_str?language_uid=python3

# a = input()
# b = input()
# if a == b:
#     print("OK")
# else:
#     print("NG")


# ⑤数の並び替え（paizaランクD 相当）
# url: none

# a = int(input("a = "))

# (内包表記)
# list = [int(input()) for _ in range(a)]

# (ノーマル)
# list = []
# for _ in range(a):
#     list.append(int(input()))

# for b in sorted(list):
#     print(b)


# ⑥閏年の判定 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/dateset/leap_year?language_uid=python3

# a = int(input())

# if a % 400 == 0:
#     print("Yes")
# elif a % 100 == 0:
#     print("No")
# elif a % 4 == 0:
#     print("Yes")
# else:
#     print("No")


# ⑦【競技1】合格判定 (paizaランク D 相当)
# url:　https://paiza.jp/works/mondai/warset/d1_pass_verdict?language_uid=python3

# a = int(input())

# if a >= 80:
#     print("pass")
# else:
#     print("fail")

# ⑧【競技1】合格判定 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/warset/d2_same_words?language_uid=python3

# a = input()
# b = input()

# if a == b:
#     print("YES")
# else:
#     print("NO")


# ⑨【競技3】深夜時間の表記 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/warset/d3_night_time?language_uid=python3

# a = int(input())
# a -= 24
# print(a)


# ⑨【競技4】明日天気にな〜れ！ (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/warset/d4_weather?language_uid=python3

# for _ in range(int(input())):
#     a = input()
#     if a == "forward":
#         print("Sunny")
#     elif a == "reverse":
#         print("Rainy")
#     else:
#         print("Cloudy")


# ⑩【競技5】ゆで卵 (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/warset/d5_egg?language_uid=python3

# a = int(input())

# if a <= 5:
#     print("raw")
# elif a <= 7:
#     print("soft boiled")
# else:
#     print("hard boiled")

# 11,【競技6】匿名希望さん (paizaランク D 相当)
# url: https://paiza.jp/works/mondai/warset/d6_initial?language_uid=python3

# a, b = input().split()
# print(a[0].upper() + "." + b[0].upper() + ".")
