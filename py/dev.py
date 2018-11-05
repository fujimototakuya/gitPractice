# 関数を作ろう
def print_test():
    print("これだけの関数")


print_test()


# 引数を使おう
def add_five(i: int):
    return i + 5


print(add_five(10))


# デフォルト引数
def print_help_message(message1='困ったら叫ぶ！',
                       message2='もっと困ったら寝る！！！'):
    print(message1)
    print(message2)


print_help_message()


# 引数の個数が不明な時
def print_help_message(mes1='困ったら叫ぶ！',
                       mes2='もっと困ったら寝る！！！'):
    print(mes1)
    print(mes2)


print_help_message()


# 戻り値を使おう
def num_input(input_message, error_message):
    # 変数numberにユーザーからの入力を受け取る
    number = input(input_message)
    # ユーザーからの入力が数値かどうかを判定
    if number.isdigit():
        return int(number)
    else:
        return error_message


num = num_input('好きな数字を入力して下さい。', 'ERROR:数値を入力して下さい。')

# ユーザーからの入力をそのまま表示
print(num)
# 　ユーザーが入力した値のデータ型を表示
print(type(num))
