1������
�����������, �ļ�һ��ʹ�� UTF-8 ���������������, �ļ�ͷ���������#--coding:utf-8--��ʶ

2�������ʽ
2.1������
ͳһʹ�� 4 ���ո��������

2.2���п�
ÿ�д��뾡�������� 80 ���ַ�(����������¿�����΢���� 80 ��������ó��� 120)

���ɣ�

���ڲ鿴 side-by-side �� diff ʱ���а��������ڿ���̨�²鿴����̫�������������ȱ��

2.3������
��˵����Ȼ����ʹ��˫���ţ�������ʾʹ�õ����ţ���� ������ ����Ӧ��ʹ�� ������

��Ȼ���� ʹ��˫���� "..."
���������Ϣ���ܶ�������� unicode��ʹ��u"�������"������ʶ ʹ�õ����� '...'
���� dict ��� key������ʽ ʹ��ԭ����˫���� r"..."�ĵ��ַ��� (docstring) ʹ������˫���� """......"""

2.4������
ģ�鼶�������ඨ��֮������У����Ա����֮���һ�У�

class A:

    def __init__(self):
        pass

    def hello(self):
        pass

def main():
    pass

����ʹ�ö�����зָ�������صĺ��������п���ʹ�ÿ��зָ����߼���صĴ���

2.5������

�ļ�ʹ�� UTF-8 �����ļ�ͷ������#-*-conding:utf-8-*-��ʶ

3��import ���
import ���Ӧ�÷�����д
# ��ȷ��д��
import os
import sys

# ���Ƽ���д��
import sys,os

# ��ȷ��д��
from subprocess import Popen, PIPE
import���Ӧ��ʹ�� absolute import

# ��ȷ��д��
from foo.bar import Bar

# ���Ƽ���д��
from ..bar import Bar
import���Ӧ�÷����ļ�ͷ��������ģ��˵����docstring֮����ȫ�ֱ���֮ǰ��import���Ӧ�ð���˳�����У�ÿ��֮����һ�����зָ�
import os
import sys

import msgpack
import zmq

import foo
��������ģ����ඨ��ʱ������ʹ����Ե���

from myclass import MyClass
�������������ͻ�����ʹ�������ռ�

import bar
import foo.bar

bar.Bar()
foo.bar.Bar()
4���ո�
�ڶ�Ԫ��������߸���һ��[=,-,+=,==,>,in,is not, and]:

# ��ȷ��д��
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# ���Ƽ���д��
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
�����Ĳ����б��У�,֮��Ҫ�пո�

# ��ȷ��д��
def complex(real, imag):
    pass

# ���Ƽ���д��
def complex(real,imag):
    pass
�����Ĳ����б��У�Ĭ��ֵ�Ⱥ����߲�Ҫ��ӿո�

# ��ȷ��д��
def complex(real, imag=0.0):
    pass

# ���Ƽ���д��
def complex(real, imag = 0.0):
    pass
������֮��������֮ǰ��Ҫ�Ӷ���Ŀո�

# ��ȷ��д��
spam(ham[1], {eggs: 2})

# ���Ƽ���д��
spam( ham[1], { eggs : 2 } )
�ֵ�����������֮ǰ��Ҫ����Ŀո�

# ��ȷ��д��
dict['key'] = list[index]

# ���Ƽ���д��
dict ['key'] = list [index]
��ҪΪ���븳ֵ����ʹ�õĶ���ո�

# ��ȷ��д��
x = 1
y = 2
long_variable = 3

# ���Ƽ���д��
x             = 1
y             = 2
long_variable = 3
5������
Python ֧�������ڵĻ��С���ʱ�����������

�ڶ������������ŵ���ʼ��
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
�ڶ������� 4 ���ո���������ʼ���žͻ��е�����
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
ʹ�÷�б�ܻ��У���Ԫ�����+.��Ӧ��������ĩ�����ַ���Ҳ�����ô˷�����

session.query(MyTable).\
        filter_by(id=1).\
        one()

print 'Hello, '\
      '%s %s!' %\
      ('Harry', 'Potter')
��ֹ������䣬��һ���а��������䣺

# ��ȷ��д��
do_first()
do_second()
do_third()

# ���Ƽ���д��
do_first();do_second();do_third();
if/for/whileһ��Ҫ���У�

# ��ȷ��д��
if foo == 'blah':
    do_blah_thing()

# ���Ƽ���д��
if foo == 'blah': do_blash_thing()
6��docstring
docstring �Ĺ淶�����䱾�����㣺

���еĹ���ģ�顢�������ࡢ��������Ӧ��д docstring ��˽�з�����һ����Ҫ����Ӧ���� def ���ṩһ����ע����˵����docstring �Ľ���"""Ӧ�ö�ռһ�У����Ǵ� docstring ֻ��һ�С�

"""Return a foobar
Optional plotz says to frobnicate the bizbaz first.
"""

"""Oneline docstring"""
����ע��
1��ע��
1.1����ע��
��#���ź��һ�񣬶�����ÿ��зֿ���ͬ����Ҫ��#���ţ�

# ��ע��
# ��ע��
#
# ��ע��
# ��ע��
1.2����ע��
����ʹ�������ո�����ֿ���ע�ⲻҪʹ���������ע��

# ��ȷ��д��
x = x + 1  # �߿�Ӵ�һ������

# ���Ƽ���д��(�������ע��)
x = x + 1 # x��1
1.3������
�ڴ���Ĺؼ�����(��Ƚϸ��ӵĵط�), ��дע�͵�Ҫ����дע�ͱȽ���Ҫ��ע�Ͷ�, ʹ�ö���ȺŸ���, ���Ը�����Ŀ, ͻ����Ҫ��

app = create_app(name, options)


# =====================================
# �����ڴ˴���� get post��app·����Ϊ !!!
# =====================================


if __name__ == '__main__':
    app.run()
2���ĵ�ע�ͣ�Docstring��
��Ϊ�ĵ���Docstringһ�������ģ��ͷ�������������ͷ����������python�п���ͨ�������doc�����ȡ�ĵ�.
�༭����IDEҲ���Ը���Docstring�����Զ���ʾ.

�ĵ�ע���� """ ��ͷ�ͽ�β, ���в�����, ���ж���, ĩ�б��軻��, ������Google��docstring���ʾ��

# -*- coding: utf-8 -*-
"""Example docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.
"""
��Ҫ���ĵ�ע�͸��ƺ�������ԭ��, ���Ǿ����������������, ���;�������ͷ���ֵ��

#  ���Ƽ���д��(��Ҫд����ԭ�͵ȷϻ�)
def function(a, b):
    """function(a, b) -> list"""
    ... ...


#  ��ȷ��д��
def function(a, b):
    """���㲢����a��b��Χ�����ݵ�ƽ��ֵ"""
    ... ...
�Ժ�������������ֵ�ȵ�˵������numpy��׼, ������ʾ

def func(arg1, arg2):
    """������д������һ�仰�ܽ�(��: ����ƽ��ֵ).

    �����Ǿ�������.

    ����
    ----------
    arg1 : int
        arg1�ľ�������
    arg2 : int
        arg2�ľ�������

    ����ֵ
    -------
    int
        ����ֵ�ľ�������

    �ο�
    --------
    otherfunc : ��������������...

    ʾ��
    --------
    ʾ��ʹ��doctest��ʽ, ��`>>>`��Ĵ�����Ա��ĵ����Թ�����Ϊ���������Զ�����

    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    """
�ĵ�ע�Ͳ�������Ӣ��, ����Ҫ��Ӣ�Ļ����ĵ�ע�Ͳ���Խ��Խ��, ͨ��һ���仰�ܰ����˵�������ģ�顢�����ࡢ���з���, ��д�ĵ�ע�͵�, Ӧ�þ���д�ĵ�ע��

