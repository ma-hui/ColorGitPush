# -*-coding:utf-8 -*-
import re

from PIL import Image
from PIL import ImageDraw


SINGLE_HEIGHT = 10
SINGLE_WIDTH = 6

Char_Empty = '-'
Char_Full = '*'
Empty_Re = '(------+\n)+'  # 修改了Char_Empty 需要修改Empty_Re,使其可以去除连续的内容的字符


# def show_tb(strtbl):
#     '''
#     输入的数组为0,1二维数组， 先不考虑存储吧
#     '''
#     for i in range(len(strtbl)):
#         # print gittb[i]
#         for dat in strtbl[i]:
#             if dat == 0:
#                 print '-',
#             elif dat == 1:
#                 print '+',
#         print(' ')

def create_image(str):
    im = Image.new('1', (SINGLE_WIDTH * len(str), SINGLE_HEIGHT), 'white')
    draw = ImageDraw.Draw(im)
    draw.text((0,0),str)
    return im

def image_to_dot(pic , width=SINGLE_WIDTH, height=SINGLE_HEIGHT):
    im = pic
    im = im.resize((width, height), Image.NEAREST)

    ret = []
    for h in xrange(height):
        li = []
        for w in xrange(width):
            gray  = im.getpixel((w, h))
            if gray != 255 :
                li.append(Char_Full)
            else:
                li.append(Char_Empty)
        ret.append("".join(li))
    dot = "\n".join(ret)
    return  dot + '\n'

def trim_dot(str):
     ret = re.sub(Empty_Re, "\n", str)
     return  ret

def show_dot_pic(strs):
    str = strs.strip(' ')
    pic = create_image(str)
    dot =  image_to_dot(pic, width=len(str) * SINGLE_WIDTH)
    tri = trim_dot(dot)
    print tri


if __name__ == '__main__':
    show_dot_pic('I LOVE YOU')

