text='''
He went to Paris
他 去 了 巴 黎
Looking for answers
寻 找 答 案
To questions that bothered him so
这 个 一 只 困 扰 他 的 问 题
He was impressive
他 很 引 人 注 目
Young and aggressive
Savin' the world on his own
But the warm summer breezes
The French wines and cheeses
Put his ambition at bay
把他的野 心 放 在 海 湾
His summers and winters
Scattered like splinters
And four to five years slipped away
四 到 五 年 散 落

Then he went to England
然 后 他 去 了 英 国
Played the piano
弹 钢 琴
And married an actress named Kim
They had a fine life, she was a good wife
And bore him young son named Jim
And all of the answers, and all the questions
He locked in his attic one day
'Cause he liked the quiet
Clean country livin' and
Twenty more years slipped away

Well, the war took his baby
Bombs killed his lady
And left him with only one eye
His body was battered
His whole world was shattered
And all he could do was just cry
While the tears were falling and he was recalling
Answers he'd never found
So he hopped on a freighter, skidded the ocean
And left England without a sound

Now he lives in the islands
Fishes the pilings
And drinks his green label each day
Writing his memoirs
Losin' his hearin'
But he don't care what most people
Through eighty-six years of perpetual motion
If he likes you he'll smile, and he'll say,
"Jimmy, some of it's magic, some of it's tragic
But I had a good life all of the way."
And he went to Paris
Lookin' for answers to questions
That bothered him so
'''
symbol = ",.!-'\""
for str in symbol:
    text = text.replace(str,'') #替换符号为空格符号
print(text)

import re
def stats_text_en(text):
    result=re.sub("[^A-Za-z]", " ", text.strip())#使用正则表达式"[a-zA-Z]+"，将非英文字母替换成空字符,text.strip()移除text中的空格符的副本
    d = {} #统计字符以及出现的次数
    for x in result.split(): #切片
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x]+1
    return d
print(stats_text_en(text)) #打印定义的函数
print("按照出现次数从大到小输出所有的单词及出现的次数")
print (sorted(stats_text_en(text).items(), key=lambda x:x[1],reverse=True))#Return a new view of the dictionary’s items ((key, value) pairs). 

import re
def states_text_cn(text):
    result=re.sub("[a-zA-Z0-9]"," ",text)#将英文字符及数字字符替换成空字符，保留汉字
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
