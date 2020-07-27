# 練習
# 秒数を変換する
time = int(input("好きな秒数を入力してください："))

h = time // 3600
m = (time - h * 3600) // 60
s = time - (h * 3600) - (m * 60)

time1 = "{}秒は、{}時間{}分{}秒です。".format(time,h,m,s)
print(time1)

print("----------")

# 秒数に戻す
h = int(input("時間を入力してください："))
m = int(input("分を入力してください："))
s = int(input("秒を入力してください："))

time2 = (h * 3600) + (m * 60) + s
ans = "{}時間{}分{}秒は、{}秒です。".format(h,m,s,time2)
print(ans)

print("----------")

if time == time2:
    print("正常に動作しています")
else:
    print("入力に間違いがあるようです")
