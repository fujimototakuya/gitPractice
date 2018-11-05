income = 1000000
if income == 1000000:
    print('!')

if income < 100000000:
    print('?')
else:
    print('!')

if income % 5 == 0 & income % 3 == 1:
    print('Hello')
elif income % 40 == 0:
    print("こんにちは")
else:
    print('Bonjour')

test_score_english = 65
test_score_math = 10
test_score_japanese = 80

if (test_score_japanese >= 70) and ((test_score_english >= 60) or (test_score_math >= 60)):
    print("合格です！")
else:
    print('次回頑張りましょう')
