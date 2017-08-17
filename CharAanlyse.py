# -*-coding:utf-8 -*-

def show_tb(gittb):
    '''
    输入的数组为0,1二维数组， 先不考虑存储吧
    '''
    for i in range(len(gittb)):
        # print gittb[i]
        for dat in gittb[i]:
            if dat == 0:
                print '-',
            elif dat == 1:
                print '+',
        print(' ')


def test():
    show_tb('a')
test()
