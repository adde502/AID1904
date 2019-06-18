# 1.	有一堆球，白球有4个，黄球有8个，黑球有12个，三种颜色的球放一起。现从中随机取出10个球，且必须有白球。编程实现：输出所有可能的取球方案，并统计总共有多少种方案。要求：
# a)	使用函数封装功能；
# b)	使用闭包结构封装功能；
# c)	使用面向对象封装功能

# 基础算法实现
# for i in range(1,5):
#     for j in range(0,9):
#         for k in range(0,10):
#             if i + j + k == 10:
#                 print(i,j,k)


# 函数封装功能
# def selectBall():
#     for i in range(1,5):
#         for j in range(0,9):
#             for k in range(0,10):
#                 if i + j + k == 10:
#                     print('可能的取球方案：白球%d个，黄球%d个，黑球%d个'%(i,j,k))

# def test():
#     selectBall()

# if __name__ == '__main__':
#     test()

# 闭包结构封装功能

# def out_():
#     white = range(1,5)
#     yellow = range(0,9)
#     black = range(0,10)
#     def in_():
#         nonlocal white,yellow,black
#         for i in white:
#             for j in yellow:
#                 for k in black:
#                     if i + j + k == 10:
#                         print('可能的取球方案：白球%d个，黄球%d个，黑球%d个'%(i,j,k))

#     return in_


# selectball = out_()
# selectball()

# 面向对象封装功能

# class SelectBall(object):
#     def __init__(self):
#         self.white = range(1,5)
#         self.yellow = range(0,9)
#         self.black = range(0,10)

#     def selectball(self):
#         for i in self.white:
#             for j in self.yellow:
#                 for k in self.black:
#                     if i + j + k == 10:
#                         print('可能的取球方案：白球%d个，黄球%d个，黑球%d个'%(i,j,k))

# res = SelectBall()
# res.selectball()


# 2.	生成一个斐波那契数列(生成20个元素即可)。要求
# a)	使用基本算法进行实现
# b)	使用递归函数进行实现
# c)	使用面向对象封装功能

# 基础算法实现

# a = 0
# b = 1
# l = [a,b]
# for i in range(18):
#     c = a + b
#     a = b
#     b = c
#     l.append(c)

# print(l)

# 递归函数实现

# def fib_num(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_num(n-1) + fib_num(n-2)

# def fib_factory():
#     l = []
#     for i in range(20):
#         l.append(fib_num(i))
#     return l

# def test():
#     fib_list = fib_factory()
#     print(fib_list)

# if __name__ == '__main__':
#     test()


# 面向对象封装功能(低内聚)

# class FibList(object):
#     def __init__(self):
#         self.l = []

#     def __fib_num(self,n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.__fib_num(n-1) + self.__fib_num(n-2)

#     def __fib_factory(self):
#         for i in range(20):
#             self.l.append(self.__fib_num(i))
#         return self.l

#     def display(self):
#         return self.__fib_factory()


# def test():
#     fiblist = FibList()
#     res = fiblist.display()
#     print(res)

# if __name__ == '__main__':
#     test()


# 3.	接上题，将生成的斐波那契序列打散为随机序列并重新按照升序进行排序。要求：使用面向对象封装功能
# 4.	接第3题，基于当前有序序列，使用二分法查找，判断某个目标元素是否在当前序列中。要求：使用面向对象封装功能。
# 5.	接第3题，基于当前有序序列，输出当前序列中出现次数最多的字符，并统计次数。要求：使用面向对象封装功能
# 6.	接第3题，基于当前有序序列，将当前随机序列按照完全二叉树的结构输出。要求：使用面向对象封装功能


from abc import ABCMeta,abstractmethod
class ListMethod(object,metaclass=ABCMeta):
    '''
        功能接口类(抽象类)，定义功能实现的公共接口
    
    '''

    @abstractmethod
    def FunctionRealization(self):
        pass


class MakeFibNum(object):
    '''
        单一职责类：创建斐波那契数

    '''
    @classmethod
    def fib_num(cls,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return MakeFibNum.fib_num(n-1) + MakeFibNum.fib_num(n-2)

class MakeFibList(object):
    '''
        单一职责类：依赖MakeFibNum类，创建斐波那契数列

    '''
    l = []
    @classmethod
    def __fib_factory(cls):
        '''
            私有方法实现封装
        
        '''
        for i in range(20):
            MakeFibList.l.append(MakeFibNum.fib_num(i))
        return MakeFibList.l

    def display(self):
        '''
            公有实例方法对外提供接口
        
        '''
        return MakeFibList.__fib_factory()

import random
class RandomList(ListMethod):
    '''
        单一职责类：随机化序列
    
    '''
    def FunctionRealization(self,l):
        random.shuffle(l)
        return l

# res = RandomList().FunctionRealization(MakeFibList().display())
# print(res)

class BubbleSort(ListMethod):
    '''
        单一职责类：对随机序列排序
    
    '''
    def FunctionRealization(self,l):
        for i in range(len(l)-1):
            for j in range(len(l)-1-i):
                if l[j] > l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]
        return l

class BinarySearch(ListMethod):

    def FunctionRealization(self,l):
        key = int(input('请输入您要查找的数字>>>：'))
        min = 0#记录列表的最小位
        max = len(l) - 1#记录列表的最大位
        if key in l:
            while True:
                center = (min + max) // 2
                if l[center] > key:
                    max = center - 1
                elif l[center] < key:
                    min = center + 1
                elif l[center] == key:
                    return '您查找的%d在当前列表中！'%key
                    break
        else:
            return '您查找的%d不在当前列表中！'%key
        
        


class ListNumMax(ListMethod):

    def FunctionRealization(self,l):
        dic = {}
        for i in l:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        iMax = 0
        iIndex = ''
        for key in dic:
            if dic[key] > iMax:
                iMax = dic[key]
                iIndex = key
        return "出现次数最多的字符是：%s,总共出现了：%d次"%(iIndex,iMax)


class CompleteTree(ListMethod):

    def FunctionRealization(self,l):
        # 提供一个初始化好的列表
        # 第一行时只有一个数
        # 每行的数字数量
        number_count=1#2  4
        # 行数
        row_number=1   #2  3
        # 遍历这个列表
        # 形成的堆结构
        print("形成的完全二叉树结构：")
        for i in range(len(l)):
            # 因为要形成一个完全二叉树，每一层(行)的元素数量为2 ** (行数-1)个
            # 使用一个巧妙的算法来实现打印出一个完全二叉树
            # 此段算法分析：
            # i = 0时，循环刚开始，因为0和number_count不等，if跳过，直接先打印arr[0]的值，10
            # i = 1时，1和1相等，执行if,number_count(每行元素个数)变为3，然后换行，行数加1，再输出arr[1] 9
            # i = 2时，2 和 3 不等，直接打印arr[2] 8
            # i = 3时，3和3相等，if执行，number_count变为7，换行，行数变为3，输出arr[3] = 7
            # ...
            # 直至程序结束
            #-----------------------------#
            if i==number_count:
                number_count += 2 ** row_number# i = 1时，a = 3
                print("\n")
                row_number += 1# i = 1时 row = 2
            #-----------------------------#
            print (l[i],end="  ")# i = 0,if跳过，直接运行这行，10被打印  i = 1时，if执行，换到第二行，打印9
            #-----------------------------#
        return "Over"



class ListMethodFactory(object,metaclass=ABCMeta):
    '''
        功能接口工厂类，各功能工厂类继承该类，并实现实例的创建及最后的调用
    
    '''
    @abstractmethod
    def createListObject(self):
        pass


class RandomListFactory(ListMethodFactory):
    def createListObject(self):
        return RandomList()

class BubbleSortFactory(ListMethodFactory):
    def createListObject(self):
        return BubbleSort()

class BinarySearchFactory(ListMethodFactory):
    def createListObject(self):
        return BinarySearch()

class ListNumMaxFactory(ListMethodFactory):
    def createListObject(self):
        return ListNumMax()

class CompleteTreeFactory(ListMethodFactory):
    def createListObject(self):
        return CompleteTree()


def test():
    list = MakeFibList().display()
    test3 = RandomListFactory().createListObject().FunctionRealization(list)
    test4 = BubbleSortFactory().createListObject().FunctionRealization(list)
    test5 = BinarySearchFactory().createListObject().FunctionRealization(list)
    test6 = ListNumMaxFactory().createListObject().FunctionRealization(list)
    test7 = CompleteTreeFactory().createListObject().FunctionRealization(list)
    print('----------第三题输出结果：生成的随机序列：-----------')
    print(test3)
    print('----------第三题输出结果：随机序列变为有序序列：-----------')
    print(test4)
    print('---------第四题输出结果：-----------')
    print(test5)
    print('----------第五题输出结果：-----------')
    print(test6)
    print('----------第六题输出结果：------------')
    print(test7)

if __name__ == '__main__':
    test()
