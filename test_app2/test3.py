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
