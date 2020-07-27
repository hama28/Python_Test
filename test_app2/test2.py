# モジュール
# 組み込みモジュール
# [Python 標準ライブラリ](https://docs.python.org/ja/3/library/index.html)

# 数学関数
import math

# pow(x,y) = x の y 乗
print(math.pow(2,3))
print(math.pow(2,6))


# 疑似乱数
import random
print(random.randint(0,100))


# 数理統計関数
import statistics

nums = [1,5,33,12,46,33,2]
# mean(平均値)
print(statistics.mean(nums))
# median(中央値)
print(statistics.median(nums))
# mode(最頻値)
print(statistics.mode(nums))


# Pythonキーワードチェック
import keyword

print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

print(keyword.iskeyword("import"))
print(keyword.iskeyword("port"))


# 他のモジュールをインポートする
import hello
hello.print_hello()
