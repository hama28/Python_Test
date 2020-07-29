# ファイル
# ファイルに書き出す
# 日本語を書き込む場合は「encoding 引数」が必要
test = open("test.txt","w",encoding="utf-8")
test.write("Pythonからこんにちは！")
test.close()

# Python osモジュール
"""
    Windowsでもmacでも正しく動作させたい場合は、トラブルを避けるために、
    osモジュールを使ってファイルパスを組み立てる。

    import os
    os.path.join("Python_Test", "test_app2", "test.txt")
    => Python_Test/test_app2/test.txt
"""


# ファイルを自動で閉じる
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("こんにちはPython")

# ファイルの読み込み
with open("test.txt","r",encoding="utf8") as f:
    print(f.read())

# ファイルのコンテンツを読み込み、リストに入れておく
my_list = []
with open("test.txt","r",encoding="utf8") as f:
    my_list.append(f.read())
print(my_list)


# CSVファイル
import csv
with open("test.csv","w",newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])
# writerowメソッドで書き出せるのは1行
# 2行書き出すなら2回呼び出す必要がある

# csvファイルの読み込み
with open("test.csv","r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
