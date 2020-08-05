# 出現する文字列を数える
# どの文字が何回出現したか数えるアルゴリズム

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)


count_characters("Dynasty")
count_characters("Tomato to mato to Tomato")
