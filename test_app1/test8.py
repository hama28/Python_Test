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
