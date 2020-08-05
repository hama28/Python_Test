## FizzBuzzは、面接でよく聞かれる質問
# 1から100の数字を出力し、
# 3の倍数のときはFizzを、
# 5の倍数のときはBuzzを、
# 3と5の倍数のときはFizzBuzzと出力するプログラム

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)