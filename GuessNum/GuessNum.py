#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import random

Rnum = random.randint(1, 100 )
print(Rnum)
Gnum = 0
try:
    while Gnum != Rnum:
        Gnum = int(raw_input('请你输入你猜测的数字：\n'))
        if Gnum > Rnum:
            print('猜的大了')
        elif Gnum < Rnum:
            print('猜的小了')
        else :
            print('猜对了')
    print('棒')
except Exception as e:
    print(e)
