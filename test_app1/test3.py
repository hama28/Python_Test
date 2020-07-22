# コンテナ

# リスト
# リストは追加・削除・変更が可能
colors = ["red","green","blue"]
print(colors)
# 追加
colors.append("yellow")
colors.append("black")
print(colors)
# 削除
colors.pop()
print(colors)
# 変更
colors[0] = "red-red"
print(colors)

# タプル
# タプルは追加・削除・変更が不可
fruits = ("apple","grape","orange")
print(fruits)
# fruits[0] = "lemon" ←実行するとエラーがでる

# リストと同じように要素の取り出しはできる
print(fruits[1])


# 辞書
# 辞書はキーとバリューのペアでできている
# 「キー：バリュー」
birthday = {"Tanaka":"0802","Yamada":"1018","Kimura":"0123","Sato":"0410"}
print(birthday)
# キーでバリューを取り出せる
print(birthday["Kimura"])
# ペアの追加
birthday["Onodera"] = "1225"
print(birthday)
# バリューの変更
birthday["Yamada"] = "1020"
print(birthday)
# ペアの削除
del birthday["Tanaka"]
print(birthday)
