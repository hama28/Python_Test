# タプル
locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

# リスト
eights = ["Edgar Allan Poe", "Chaarles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)

# 辞書
bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

my_list = [bday]
print(my_list)

my_tuple = (bday,)
print(my_tuple)

# 組み合わせ
ny = {"座標": (40.7128, 74.0059),  # タプル(変更不可)
      "セレブ": ["ウッディ・アレン", "ジェイ・Z", "ケヴィン・ベーコン"],  # リスト(追加可能)
      "事実": {"州": "ニューヨーク", "国": "アメリカ", }}  # 辞書(ペアで扱いやすい)

print(ny)
print("セレブ" in ny)  # セレブがあるか確認
print(ny["セレブ"])  # セレブの要素を取り出す
