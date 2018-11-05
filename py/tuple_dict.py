# タプルの作成
tpl1 = (1, 2, 3, 4, 5)
print(tpl1)
a, b, c, d, e = tpl1
print(c)

# dictの説明
dict1 = {"one": 1, "tow": 2, "three": 3}
print(dict1["one"])
print(len(dict1))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
dict1["four"] = 4

dict2 = {"five": 5, "six": 6, "seven": 7}

dict1.update(dict2)
print(dict1)
