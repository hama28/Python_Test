import random

def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|       |       ",
              "|       |       ",
              "|       0      L",
              "|      /|\     O",
              "|      / \     S",
              "|              E",
              "|______________R"
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングドマンへようこそ！\n３文字を予想して当ててね！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を入力してね(半角英数)："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print("わお！ {} は答えのひとつだよ！".format(char))
        else:
            wrong += 1
            print("おしい！ {} は違うみたい！".format(char))
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("\nお見事！\nあなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
#        print("\n".join(stages[0:wrong+1]))
        print("\n残念！あなたの負け！\n正解は {} でした！".format(word))

quest = ["cat","dog","rat","pet","ant","fox","pig","cow","bug"]

hangman(random.choice(quest))
