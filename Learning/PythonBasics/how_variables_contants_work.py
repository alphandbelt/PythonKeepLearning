# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：how_variables_contants_work.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/29 13:56 
'''

"""

    1. 注释 (Comments)
    2. 常量 (Literal Constants)
    3. 变量 (Variables)
    4. 格式化字符串 (Formatted Strings)
    5. 对象 (Object)
    6. 列表 (List)
    7. 元组 (Tuple)
    8. 集合 (Set)
    9. 字典 (Dictionary)
    10. 缩进 (Indentation)
    10. 运算符和表达式 (Operators and Expressions)
        10.1 算术运算符 (Arithmetic Operators)
            10.1.1 加法运算符 (Addition Operator)
                    Plus(+)
            10.1.2 减法运算符 (Subtraction Operator)
                    Minus(-) 
            10.1.3 乘法运算符 (Multiplication Operator)
                    Multiply(*)
            10.1.4 除法运算符 (Division Operator)
                    Divide(/)
            10.1.5 取余运算符 (Modulus Operator)
                    Modulus(%)
            10.1.6 幂运算符 (Exponent Operator)
                    Exponent(**)
            10.1.7 取整运算符 (Floor Division Operator)
                    Floor Division(//)
            
        10.2 比较运算符 (Comparison Operators)
            10.2.1 等于运算符 (Equal Operator)
                    Equal(==)
            10.2.2 不等于运算符 (Not Equal Operator)
                    Not Equal(!=)
            10.2.3 大于运算符 (Greater Than Operator)
                    Greater Than(>)
            10.2.4 小于运算符 (Less Than Operator)
                    Less Than(<)
            10.2.5 大于等于运算符 (Greater Than or Equal Operator)
                    Greater Than or Equal(>=)
            10.2.6 小于等于运算符 (Less Than or Equal Operator)
                    Less Than or Equal(<=)
                    
        10.3 赋值运算符 (Assignment Operators)
            10.3.1 简单赋值运算符 (Simple Assignment Operator)
                    Simple Assignment(=)
            10.3.2 加法赋值运算符 (Addition Assignment Operator)
                    Addition Assignment(+=)
            10.3.3 减法赋值运算符 (Subtraction Assignment Operator)
                    Subtraction Assignment(-=)
            10.3.4 乘法赋值运算符 (Multiplication Assignment Operator)
                    Multiplication Assignment(*=)
            10.3.5 除法赋值运算符 (Division Assignment Operator)
                    Division Assignment(/=)
            10.3.6 取余赋值运算符 (Modulus Assignment Operator)
                    Modulus Assignment(%=)
            10.3.7 幂赋值运算符 (Exponent Assignment Operator)
                    Exponent Assignment(**=)
            10.3.8 取整赋值运算符 (Floor Division Assignment Operator)
                    Floor Division Assignment(//=)
                    
        10.4 逻辑运算符 (Logical Operators)
            10.4.1 与运算符 (And Operator)
                    And(and)
            10.4.2 或运算符 (Or Operator)
                    Or(or)
            10.4.3 非运算符 (Not Operator)
                    Not(not)
                    
        10.5 位运算符 (Bitwise Operators)
            10.5.1 与运算符 (Bitwise And Operator)
                    Bitwise And(&)
            10.5.2 或运算符 (Bitwise Or Operator)
                    Bitwise Or(|)
            10.5.3 非运算符 (Bitwise Not Operator)
                    Bitwise Not(~)
            10.5.4 异或运算符 (Bitwise XOR Operator)
                    Bitwise XOR(^)
            10.5.5 左移运算符 (Bitwise Left Shift Operator)
                    Bitwise Left Shift(<<)
            10.5.6 右移运算符 (Bitwise Right Shift Operator)
                    Bitwise Right Shift(>>)
        10.6 成员运算符 (Membership Operators)
            10.6.1 in 运算符 (in Operator)
                    in
            10.6.2 not in 运算符 (not in Operator)
                    not in
                    
        10.7 身份运算符 (Identity Operators)
            10.7.1 is 运算符 (is Operator)
                    is
            10.7.2 is not 运算符 (is not Operator)
                    is not        
        
            
        
    11. 条件语句 (Conditional Statements)
        if 语句 (if Statements)
        if-else 语句 (if-else Statements)
        if-elif-else 语句 (if-elif-else Statements)
        嵌套 if 语句 (Nested if Statements)
       
        
    12. 循环语句 (Loop Statements)
        while 循环 (while Loop)
        for 循环 (for Loop)
        嵌套循环 (Nested Loops)
        循环控制语句 (Loop Control Statements)
            break 语句 (break Statement)
            continue 语句 (continue Statement)
            pass 语句 (pass Statement)
    13. 函数 (Functions)
        
    14. 模块 (Modules)
        
    15. 包 (Packages)
    16. 类 (Classes)
    17. 异常 (Exceptions)
    18. 文件 (Files)
    19. 装饰器 (Decorators)
    20. 迭代器 (Iterators)
    21. 生成器 (Generators)
    22. 协程 (Coroutines)
    23. 多线程 (Multithreading)
    24. 多进程 (Multiprocessing)
    25. 正则表达式 (Regular Expressions)
    26. 网络编程 (Network Programming)
    27. 数据库 (Database)
    28. 时间和日期 (Time and Date)
    29. 日志 (Logging)
    30. 调试 (Debugging)
    31. 测试 (Testing)
    32. 性能 (Performance)
    33. 并发 (Concurrency)
    34. 并行 (Parallelism)
    35. 代码风格 (Code Style)
    36. 文档 (Documentation)
    37. 代码质量 (Code Quality)
    38. 代码混淆 (Obfuscation)
    39. 代码优化 (Optimization)
    40. 代码保护 (Protection)
    41. 代码加密 (Encryption)
        
    42. 代码压缩 (Compression)
        在Python中，你可以使用pyinstaller、py2exe（Windows环境）、py2app（macOS环境）等工具来将
        Python代码压缩成可执行文件。
        这些工具可以将你的Python脚本及其依赖项打包成一个独立的可执行文件，无需用户安装Python解释器。








"""





























