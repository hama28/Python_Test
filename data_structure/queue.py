## キュー
# リストのようなデータ構造
# 例 [1,2,3]

# リストと異なる点
# 要素の追加や削除が先端にしか行えない
# つまり、待ち行列のようなもの

# ファーストイン・ファーストアウト（FIFO）

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

a_queue = Queue()
print(a_queue.is_empty())

for i in range(5):
    a_queue.enqueue(i)
print(a_queue.size())

while a_queue.size():
    print(a_queue.dequeue())
print()
print(a_queue.size())