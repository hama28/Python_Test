def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|       |       ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングドマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))


hangman("cat")



"""
    --------------------
    def 関数のセッティング
    --------------------
    まず、hangmanという関数を作成
    hangmanはwordという引数を受け取る
    wordはプレイヤーに当ててほしい単語を入れる
    変数wrongはプレイヤーが何回間違えたか数える変数
    変数stagesは文字列のリスト
        これを使って、吊られた人を表示していく
    変数rlettersはwordの文字を1文字ずつの要素に分解してリストにしたもの
        残りの文字数を覚えておくのに使う
    変数boardは文字列のリストで、プレイヤーに見せるヒントを記録する
        例)答えがcatのとき、cとtを当てたら、c_tと表示するために使う
            答え(cat)のとき、boardの初期状態は["_", "_", "_"]
    変数winは初期状態ではFalseを割り当て、プレイヤーがゲームに勝ったかどうかの状態を記録させる
    「ハングドマンへようこそ！」
    --------------------
    while ループの開始
    --------------------
    wrong変数(間違った回数)が、stagesのリスト数よりも小さい間、ループを繰り返す
        -1 しているのは、wrongは１から数えるが、stagesはリストなので０から数えるのを合わせている
    見た目を良くするために空行を入れて
    inputで入力させる
    入力された内容は char に入れる
    --------------------
    if 条件分岐
    --------------------
    入力された内容(char)が、rletters(正解の文字列を持っている)にあれば正解！
    boardの内容を更新する
        例えば、c を入力したら、["c", "_", "_"] に更新する
    indexメソッドを使って、入力された文字が何番目にあるかを取得
    取得した○番目のboradの文字を、入力された文字に変更する
        ※indexメソッドは最初に見つけた要素のインデックス値しか返さない
        なので、答えに同じ文字があると正しく動作しない
            例えば、答えが pop だったりすると2回目の p の入力が動作しなくなる
    rlettersの正解した文字を＄記号に置き換えることで、次のループではindexメソッドが次の文字を返してくれる
    回答が間違っていたら、wrongをインクリメントする
    --------------------
    出力 スコアボードとハングドマン
    --------------------
    スコアボード(board)を出力
    ハングドマン(stages)を出力
        ゲームの進行に合わせてハングドマンを出力するために、stagesリストの一部をスライスで取り出す
            例
                e = 2
                print(stages[0:e])
            この場合、stagesリストの０から１までを出力する
            ※ 終了インデックスの手前の要素まで
    --------------------
    勝敗判定
    --------------------
    boardリストに "_" が無い = 全ての文字を正解した --> プレイヤーの勝利
    「あなたの勝ち！」
    正解を表示して
    win を True に変更
    break でループを終了させる
    --------------------
    ループ終了
    --------------------
    ループが終了しても、win が False の場合は、プレイヤーの負け
    ハングマンの絵を全て表示し
    「あなたの負け！」
    正解の表示
"""