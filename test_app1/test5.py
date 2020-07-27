# コンテナの中にコンテナ

# 空のコンテナ作成
lists = []

# 入れるコンテナ作成
rap = ["カニエ・ウェスト", "ジェイ・Z", "エミネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]

# コンテナの中に追加
lists.append(rap)
lists.append(rock)
lists.append(djs)

# 追加されてるか確認
print(lists)

# 親コンテナの最初の要素にrapが入っている
print(lists[0])

# rapに追加して、親に反映されるか確認
rap.append("ケンドリック・ラマー")
print(lists)
