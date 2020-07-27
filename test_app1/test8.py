# 分割
kot = "水たまりを飛び越えたんだ。3メートルもあったんだぜ！".split("。")
print(kot)

# 結合
# すべての文字列の間に追加する
firsr_three = "abcdefg"
result = "+".join(firsr_three)
print(result)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words)
print(one)

# 空白除去
s = "  The     Fox   "
print(s)
s = s.split()
print(s)

# 置換
equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

# 文字を探す
ani = "animals".index("m")
print(ani)

try:
    anime = "anime".index("z")
    print(anime)
except:
    print("Not found.")

# 包含
azu = "Cat" in "Cat in the hat."
print(azu)
azu = "Bat" in "Cat in the hat."
print(azu)

pot = "Potter" not in "Harry"
print(pot)
pot = "Potter" not in "HarryPotter"
print(pot)

# エスケープ文字
bot = "彼女は\"そうだね\"と言った"
print(bot)
bot = "彼女は'そうだね'と言った"
print(bot)
bot = '彼女は"そうだね"と言った'
print(bot)

# 改行
line = "line1\nline2\nline3"
print(line)

# スライス
fict = ["トルストイ","カミュ","オーウェル","ハクスリー","オースティン"]
print(fict[0:3])

ivan = "死の代わりにひとつの光があった"
print(ivan[0:6])
print(ivan[6:16])

gene = "はじめに神は天と地とを創造された。地は形なく、むなしく、やみが淵のおもてにあり、神の霊が水のおもてをおおっていた。神は「光あれ」と言われた。すると光があった。"
print(gene[:17])
print(gene[17:57])
print(gene[57:])
