# アナグラム
# 単語の文字を並び替えて別の単語を作ること
# 例
# iceman = cinema

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


print(anagram("iceman", "cinema"))
print(anagram("Kyoto", "Tokyo"))

# sorted関数に渡して、アルファベット順に並べ替える
# 並べ替え単語２つを比較して、一致したらTrueを、不一致ならFalseを返す
