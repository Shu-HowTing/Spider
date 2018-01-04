'''
yield
生成器的优势:
    节省存储空间
    更快的响应速度
    使用更加灵活
'''

#yield写法
def gen(n):
    for i in range(n):
        yield i**2

for i in gen(5):
    print(i, ' ', end='') #0  1  4  9  16

print('')
#对比
#普通写法
def gen(n):
    lst = [i**2 for i in range(n)]
    return lst

for i in gen(5):
    print(i, ' ', end='') #0  1  4  9  16

