# 计算并输出输出1000以内的”水仙花数“
print('1000以内的水仙花数有：',end='')#end= 指定print以什么结束，（默认是换行）
for n in range(100,1000):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if n == a**3 + b**3 + c**3:
        print(n,end='  ')