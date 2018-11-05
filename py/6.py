list= ['apricot', 'strawberry', 'fig', 'orange', 'persimmon', 'cantaloupe', 'kiwifruits', 'guava', 'cranberry',
       'grapefruit', 'cherry', 'pomegranate', 'watermelon', 'plum', 'gooseberry', 'dragon fruits', 'pear',
       'pineapple', 'passion fruit', 'banana', 'papaya', 'grape', 'blackberry', 'blueberry', 'mango', 'melon',
       'peach', 'raspberry', 'apple', 'lychee', 'lime', 'lemon', ]

value=[]


for s in list:

        a = s[0]

        value.append(a)

d = dict(zip(list, value))

d = sorted(d.items())

print(d)