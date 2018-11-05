import random
from statistics import mean, median,stdev
from collections import Counter

list=[]

for i in range(1000):

    x=random.randint(1,6)
    list.append(x)
    if i== 1000:
        break

def calculate_mode(list):
    c = Counter(list)
    freq_scores = c.most_common()
    max_count = freq_scores[0][1]
    modes = []

    for num in freq_scores:
        if num[1] == max_count:
            modes.append(num[0])
    return(modes)

if __name__ == '__main__':
    list
    modes = calculate_mode(list)

    for mode in modes:
        s=mode


m = mean(list)
median = median(list)
stdev = stdev(list)



# print(list)
print('平均: {0:.2f}'.format(m))
print('中央値: {0:.2f}'.format(median))
print('最頻値は'+str(s))
print('標準偏差: {0:.2f}'.format(stdev))


