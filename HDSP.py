from unit.test_demo import Test_Demo

import pytest

print('c:\some\\name')

print('py', 'thon')

squares = [1, 4, 9, 24]
squares

"""
1.列表数据结构squares
列表的基本操作：append，inset，remove，pop、sort
2.堆栈用法：append(追加) 、pop(弹出来),后进先出
squares.append

3.队列用法：先进先出 deque
deque.append 、deque.popleft
4.列表创建：list=[x*10 for x in range(10)]公式

5.集合：sets 无排序
basket.add 添加
basket.union 取交集
baseket.difference() 找出与另外一个列表没有的数据
6.元祖：Tuples 不可修改，用来传参


7.列表：Lists可修改

8.词典：Dictionaries关系数据   for in 结构

"""

"""
创建git 仓库远程链接  用户名caoyu110110 密码caoyu19934250

git init 添加仓库
git add README.md 添加说明文件（帮助文档）
git commit -m "first commit" 提交文件
git branch -M main
git remote add origin git@github.com:caoyu110110/HDSP.git  本地仓库与远程仓库建立连接
git push -u origin main   同步代码到远程仓库

创建仓库遇到的问题； 
 OpenSSL SSL_read: Connection was reset, e
rrno 10054或者超时，重新下载git最新版本，提示到浏览器去登陆即可
"""
"""
if
elif
else
例子
"""
x = input("您好，请输入您编写自动化测试用例常用的测试框架：")
if x == "pytest":
    print("高级测试工程师")
elif x == "unitest":
    print("中级测试工程师")
else:
    print("不符合要求")
"""
for 计数循环
"""
interviewee = [26, 28, 30, 32, 26, 35, 40]
for i in range(5):
    if 30 < interviewee[i] < 35:
        print(f"第{i}名面试：{interviewee}岁可能成为高级工程师")
    elif interviewee[i] >= 35:
        print(f"第{i}名面试：{interviewee}岁可能成为测试管理专家")
    else:
        print(f"第{i}名面试：{interviewee}岁可能成为初级工程师")
"""
函数
def fun(a,b=1,*c,**d):
        a :任意值
        b:默认值
        c:词典参数，命名参数
        d:变长参数，参数拆箱
...     print(f'a={a}\nb={b}\nc={c}\nd={d}')
... fun(1,2,3,4,5)
"""

"""
类与方法
class Myclass:
@classmethod 标记一个方法 可以允许不用实例化，变成一个类变量



python标准库unitest
集成测试框架Pytest
测试装置 用例执行顺序控制
setup_module 
@class_method
setup_method
setup_function
teardown_
pytest_order

分组控制
@pytest.mark
@pytest.mark.ringt
@pytest.mark.exception
"""


