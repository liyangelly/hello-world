text='''

How The Foolish Old Man Moved Mountains
愚 公 移 山 与 红 衣 衫
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads to
Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his
wife. “How on earth do you suppose you can level Mount Taixin and
Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea of
Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full
year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for
his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,
and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never
understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my
grandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will not
grow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and
his crew were, they were struck with fear and reported the incident
to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two
mighty gods to carry the mountains away.

'''
symbol = ",.!-'\""
for str in symbol:
    text = text.replace(str,'') #替换符号为空格符号
print(text)

import re
def stats_text_en(text):
    result=re.sub("[^A-Za-z]", " ", text.strip())#使用正则表达式"[a-zA-Z]+"，将非英文字母替换成空字符
    d = {} #统计字符以及出现的次数
    for x in result.split(): #切片
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x]+1
    return d
print(stats_text_en(text)) #打印定义的函数
print("按照出现次数从大到小输出所有的单词及出现的次数")
print (sorted(stats_text_en(text).items(), key=lambda x:x[1],reverse=True))

import re
def states_text_cn(text):
    result=re.sub("[A-Za-z0-9]"," ",text) #过滤字符串中的英文与符号，保留汉字
    d = {} #统计字符以及出现的次数
    for x in result.split(): #切片
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x]+1
    return d
print(states_text_cn(text)) #打印定义的函数
print("按照出现次数从大到小输出所有的单词及出现的次数")
print (sorted(states_text_cn(text).items(), key=lambda x:x[1],reverse=True))
