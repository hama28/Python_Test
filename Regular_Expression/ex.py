import re

# シンプルな一致
l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

# 前方一致
zen = """Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

# 複数文字との一致
# ( t から始まって、次に o か w がきて、次に o がくる)
string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

# 数値との一致
# (Unix系では、[[:digit]] )
line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

# 繰り返し
# (非貪欲な正規表現)
t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

# Mad Libsゲーム
# 入力された内容を虫食いに入れて表示させる
text = """キリンは大昔から __職業__ の興味の対象でした。
キリンは __〇〇類__ の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって
獲得したのか説明できませんでした。キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と
 __体の一部__ によるものです。
"""
def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)

# エスケープ
# (例えば $ は、行の終端に一致するパターンを作るが、
# エスケープすることで、ドル記号そのものに一致する)
line = "I love $ money"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)