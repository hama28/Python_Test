# 文字列操作

# 三重クォート
""" line one
    line two
    line three
"""

# 文字の取り出し
author = "Kafka"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

# 文字の連結
cat = "cat" + " in" + " hat"
print(cat)

# 文字のかけ算
sat = "GoTo " * 3
print(sat)

# 大文字・小文字
gat = "We hold these truths...".upper()
print(gat)
jat = "SO IT GOES.".lower()
print(jat)

# 最初の文字だけ大文字に。キャピタライズ
dat = "four score AND...".capitalize()
print(dat)

# 書式化
# あとで穴埋めする
fat = "こんにちは、{}".format("ウィリアム・フォークナー")
print(fat)

# 変数も渡せる
name = "ウィリアム・フォークナー"
rat = "こんにちは、{}".format(name)
print(rat)

# {}は何回でも書ける
year_born = "1897"
bat = "{}は{}年に生まれました。".format(name, year_born)
print(bat)

# 入力した文字を使って文字列の組み立て
what = input("何が；")
when = input("いつ：")
where = input("どこで：")
do = input("どうした：")
textline = "{}は{}に{}で{}。".format(what, when, where, do)
print(textline)
