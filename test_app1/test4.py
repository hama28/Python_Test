songs = {"1": "mirai",
         "2": "time",
         "3": "only",
         "4": "time",
         "5": "live"}

n = input("数字を入力してください(1～5)：")

if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません。")
