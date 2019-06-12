#ֵ使用for/while循环打印九九乘法表，while循环需要剔除偶数的行
a = 0 #创建整数型变量
b = 0 #创建整数型变量
x = input('请选择控制结构[for/whilewhile]' '\n') #选择控制结构
if x == 'for': #选择控制结构为for循环时使用
    for a in range(1,10): #外层for循环1-9，控制行数
        for b in range(1,a):      #内层for循环1-a-1,控制列数
            print(a,'*',b,'=',a*b,end='\t') #输出非最后一列的值，中间用制表符隔开
        print(a,'*',b+1,'=',a*(b+1)) #输出最后一列的值，用换行符换行
elif x == 'while': #选择控制结构为while时使用
    for a in range(1,10,2):#从1开始，步数为2，到10之前结束
        for b in range(1,a):
            print(a,'*',b,'=',a*b,end='\t')
        print(a,'*',b+1,'=',a*(b+1))

  