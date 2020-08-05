# 線形探索
# データ構造の中の要素を１つひとつ確認して探しているものを見つける
# シンプルな探索アルゴリズム
# カードゲームでデッキから1枚探すときみたいな感じ

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)
