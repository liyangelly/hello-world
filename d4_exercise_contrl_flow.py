#ֵ使用for/while循环打印九九乘法表，while循环需要剔除偶数的行
a = 0 #创建整数型变量
b = 0 #创建整数型变量
x = input('请选择控制结构[for/while]' '\n') #选择控制结构
if x == 'for': #选择控制结构为for循环时使用
    for a in range(1,9): #外层for循环1-9，控制行数
        for b in range(1,a+1):      #内层for循环1-a-1,控制列数
            print(a,'*',b,'=',a*b,end='\t') #输出非最后一列的值，中间用制表符隔开
            if b == a:
                print(end='\n')
elif x == 'while': #选择控制结构为while时使用
    a = 1
b = 1
while(a<10):
    while(a%2 != 0):
        while(b <= a):
            print(a,'*',b,'=',a*b,end='\t')
            b=b+1
        else:
            print(end='\n')
        break
    a += 1
    b=1

            
  