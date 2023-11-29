


"""
        python函数

        定义 def
        参数，返回值
        内置函数 len() print() intput()

        作用域
        全局变量

        递归函数
        匿名函数
        装饰器

        内置函数：python语言本身提供的函数

        print()
        len()
        input()
        float()
        str()
        list()
        tuple()

        set()
        range()
        abs()  绝对值
        round() 四舍五入
        max() 返回给定参数的最大值
        min()
        min([1,2,3,4])  1

        sorted([1,3,2,5])
        type()
        python异常处理

        try:
            do_something()
        except Exception as e:
            print(e)
"""

a = 123
def test_func(pams):
    print("这是一个函数")
    print("这是函数的参数", pams)
    global a
    a = 234
    return "这是函数的返回值"

b = test_func("123")
print("改变后的a",a)
print(b)


try:
    a = 1 / 0
except Exception as e:
    print(e)

print(a)








