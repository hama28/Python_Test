# 回文
# 初めから読んでも終わりから読んでも同じになる文章

def palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(palindrome("Mother"))
print(palindrome("Mom"))

# word[::-1]
# Pythonの文法で、シーケンス全体のスライスを逆順で返す
