## スタック
# リストのようなデータ構造
# 例 [1,2,3]

# リストと異なる点
# 要素の追加や削除が終端にしか行えない
# つまり、積み重ねた皿のようなもの

# ラストイン・ファーストアウト（LIFO）

# スタックから要素の削除 = ポップ
# スタックに要素の追加 = プッシュ

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        # return self.items == []
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        # last = len(self.items) - 1
        # return self.items[last]
        return self.items[-1]
    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())
# 最初は空なのでTrueを返す

stack.push(1)
print(stack.is_empty())
# 要素が追加されたので、空じゃない=Falseを返す

item = stack.pop()
print(item)
print(stack.is_empty())
# 要素を削除したので、空になり=Trueを返す

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())
# 覗き見(peek)でstackの終端をチェック
# sizeで全体のカウント