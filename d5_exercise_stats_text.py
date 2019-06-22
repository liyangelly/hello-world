text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
a= text.replace(',', ' ').replace('.', ' ').replace(  '--', ' ').replace('!', ' ').replace('*', ' ') #标点符号替换为空格
b= a.split() #按照空格进行分割成单个的单词

c={}#按照{'is':10,'better': 9, ...}摆放
for i in b: 
    d=b.count(i)#i出现的次数
    e={i:d}#摆放顺序
    c.update(e)#迭代？？

f=sorted(c.items(),key=lambda x:x[1],reverse=True) # key=lambda  变量：变量[维数] 。维数可以按照自己的需要进行设置。按前面的value值排序
print(f)