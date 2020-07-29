## chapter9 challenge
import csv

# 質問を表示し、入力された回答をファイルに書き出す
ans = input("好きなフルーツを教えて下さい：")
with open("challenge1.txt","w",encoding="utf8") as f:
    f.write(ans)

# リストのリストに含まれる要素をCSVファイルに書き出す
movie = [["Top Gun","Risky Business","Minority Report"],
         ["Titanic","The Revenant","Inception"],
         ["Training Day","Man on Fire","Flight"]]

with open("challenge1.csv","w",newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(movie[0])
    w.writerow(movie[1])
    w.writerow(movie[2])

# 日本語で同じようにCSVファイルに書き出す
sw = [["ファントム・メナス","クローンの攻撃","シスの復讐"],
      ["新たなる希望","帝国の逆襲","ジェダイの帰還"],
      ["フォースの覚醒","最後のジェダイ","スカイウォーカーの夜明け"]]

with open("challenge2.csv","w",newline='',encoding="utf8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(sw[0])
    w.writerow(sw[1])
    w.writerow(sw[2])
