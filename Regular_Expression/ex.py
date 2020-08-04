import re

# シンプルな一致
l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

# 前方一致
zen = """Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

# 複数文字との一致
# ( t から始まって、次に o か w がきて、次に o がくる)
string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

# 数値との一致
# (Unix系では、[[:digit]] )
line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)