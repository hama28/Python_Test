# 再帰
# 大きな問題を小さな問題に分割して解決する
# 再帰法
# 関数からその関数自体を呼び出す手法
# 再帰関数と呼ぶ
# 再帰関数は、無限に呼び出し続けたり(無限再帰)しないように、
# 関数自身の呼び出しを終了する条件である、再帰終了条件を持たなければいけない
# 再帰のルール
# 1) 再帰法は、再帰終了条件を持たなければならない
# 2) 再帰法は、状態を変えながら再帰終了条件に進んでいかなければならない
# 3) 再帰法は、再帰的に関数自身を呼び出さなければならない

def bottles_of_bear(bob):
    """Prints Bottle of Bear on the Wall lyrics.

    :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("""No more bottles of bear on the wall.
              No more bottles of bear.""")
        return

    tmp = bob
    bob -= 1
    print("""{} bottles of bear on the wall.
          {} bottles of bear.
          Take one down, pass it around,
          {} bottles of bear on the wall.
          """.format(tmp, tmp, bob))
    bottles_of_bear(bob)


bottles_of_bear(99)
