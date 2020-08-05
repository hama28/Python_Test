class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
# 文字を1文字ずつスタックに追加していく
for c in "Hello World":
    stack.push(c)

reversed_string = ""

# スタックの要素を終端から1文字ずつ追加していく
for i in range(len(stack.items)):
    reversed_string += stack.pop()

print(reversed_string)