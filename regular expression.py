import re

'''
正则表达式:

P(Y|YT|YTH)?N   'PN' 'PYN' 'PYTHN'
PYTHON+         'PYTHON' 'PYTHONN'  'PYTHONNN' ....
PY[TH]ON        'PYTON'   'PYHON'
PY[^TH]?ON      'PYON'  'PYaON' 'PYbON' ....
.....
'''
'''
正则表达式表示类型：
    原生字符串类型（不包括转义字符） r'text'
    r'[1-9]\d{5}'  #表示邮政编码

'''
#re主要函数

#re.search(pattern, string, flags=0)  返回一个match对象
#注意：search函数只返回满足条件的第一个字符串
match = re.search(r'[1-9]\d{5}', '100081 ueiin 103081 china')
if match:
    print(match.group())

#re.match(pattern, string, flags=0)    返回一个match对象
#match函数从待匹配的字符串的起始位置就开始匹配， 即如果待匹配的字符串的
#第一个字符串如果和正则表达式的首字符匹配不上，则返回空，不继续匹配
match = re.match(r'[1-9]\d{5}', '100081 ueiin 103081 china')
if match:
    print(match.group())

#比较
match = re.match(r'[1-9]\d{5}', 'ueiin 103081 china')
if match:
    print(match.group())
else:
    print(None)

#re.findall()  返回列表类型
l1 = re.findall(r'[1-9]\d{5}', '100081 ueiin 103081 china')
print(l1)  #['100081', '103081']

#re.split()  #返回列表   把正则表达式看成分隔符， maxsplit参数控制分割数
l2 = re.split(r'[1-9]\d{5}', 'BAT100081 ueiin 103081 china')
print(l2)
l3 = re.split(r'[1-9]\d{5}', 'BAT100081 ueiin 103081 china', maxsplit=1)
print(l3)

#re.finditer()
#返回一个匹配结果的迭代类型，每个迭代元素都是一个match对象
for m in re.finditer(r'[1-9]\d{5}', 'BAT100081 ueiin 103081 china'):
    if m:
        print(m.group())

#re.sub() 将正则表达式替换成目标字符串， 返回替换后的字符串
#re.sub(pattern, repl, string, count=0, flags=0)
str = re.sub(r'[1-9]\d{5}', '!', 'BAT100081 ueiin 103081 china')
print(str)   #BAT! ueiin ! china

'''
re.compile()
将正则表达式字符串编译成正则表达式对象
当多次使用时，比较方便
'''
pat = re.compile(r'[1-9]\d{5}')
match = pat.search('BAT100081 ueiin 103081 china')
if match:
    print(match.group())

'''
match 对象的常用属性
    .string: 带匹配的文本  string
    .re: 正则表达式
    .pos: 正则表达式搜索文本的开始位置
    .endpos: 正则表达式文本的结束位置
match 对象的常用方法
    .group():获得匹配后的字符串
    .start():匹配字符串在原始字符串中的起始位置
    .end():匹配字符串在原始字符串中的结束位置
    .span(): 返回(.start(), .end())
'''
pat = re.compile(r'[1-9]\d{5}')
match = pat.search('BAT100081 ueiin 103081 china')
#match = re.search(r'[1-9]\d{5}', '100081 ueiin 103081 china')
print(match.string)
print(match.re)
print(match.pos) #0
print(match.endpos)

print(match.start())
print(match.span())

#贪婪匹配和最小匹配
#贪婪匹配，输出最长的字符串
match = re.search(r'PY.*N', 'PYANBNCNDN')
print(match.group()) #PYANBNCNDN
#最小匹配
#*?   +?    ??  ...
match = re.search(r'PY.*?N', 'PYANBNCNDN')
print(match.group()) #PYAN













































