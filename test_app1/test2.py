mozi = ["A","B","C","D","E"]
print(mozi)

if "E" in mozi:
    print("moziにEが存在します")

if "Z" not in mozi:
    print("moziにZは存在しません。Zを追加します。")
    mozi.append("Z")

print(mozi)
