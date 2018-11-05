# whileに関するエトセトラ

# 基本的な何か
cnt = 0
while cnt < 100:
    print(cnt)
    cnt += 1

# inputを使った何か
end = 0
while end == 0:
    print("ぐるぐる")
    end = input("ループを終了するには0以外を入力してください")
    end = float(end)

# break を使う
while True:
    print("1回のみ")
    break

# continueを使う
cnt = 0
while cnt < 5:
    cnt += 1
    if cnt == 2:
        print('cnt=2の時は以下のコメントをスキップ')
        continue
    print("もう一回")
