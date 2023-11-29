"""
    TODO:    实际操作python的变量和数据类型 演示

"""
import datetime
import time

# int (整型)

apple = 10
banana = 20
count = apple + banana

print("香蕉和苹果总共有", count)
print(type(count))

# float（浮点型）

a = 0.618
b = 0.382
c = a + b
print("c=", c)
print(type(c))

# complex


str = "这是一个字符串"
str1 = '这也是一个字符串'
str2 = "'这是一个包含单引号的字符串'"
str3 = '"这是一个包含双引号的字符串"'

str4 = """
     这是第一行
     这是第二行
     这是第三行
    
     这是空格之后的第四行
        

"""

print(str, str1, str2, str3)
print(str4)

# bool （true，false）

bool_a = 1
bool_b = 0

if bool_a:
    print("bool_b:", bool_b)

if bool_b:
    print("bool_a:", bool_a)

str5 = "str5"
str6 = ""

if str5:
    print("str5:", str5)

if str6:
    print("str6:", str6)

# list

apple_list = ["apple", "apple2", "apple3"]
banana_list = ["banana1", "banana2", 2, "b3"]

print("apple_list:", apple_list)
print("banana_list:", banana_list)

# index
print("apple_list的第一个值：", apple_list[0])
print("banana_list的第一个值：", banana_list[0])

print("apple_list的第一个和二个值：", apple_list[0:3])
print("apple list的最后一个值：", apple_list[-1])

apple_list_len = len(apple_list)
print("apple list总共有多少个元素:", apple_list_len)
print("banana list  总共有多少个元素:", len(banana_list))

apple_list.append("apple4")
apple_list.append("apple5")

print("apple_list:", apple_list)

apple_list[-1] = "apple修改后的第五个元素"

print(apple_list)

#  循环
# for
for apple in apple_list:
    print(apple, apple_list.index(apple))

# while


# count = 1
#
# while True:
#     print(datetime.datetime.now())
#     time.sleep(1)
#     count = count + 1
#     if count > 10:
#         break

# tuple

# 不能被改变
tuple1 = ("123", "12", "元组变量3")

# dict key-value
dict1 = {
    "name": "wangerxiao",
    "age": 18,
    "height": "183cm",
    "address": "四川省xxx街道",
    "phone_number": "1101208970"

}

print("姓名：", dict1["name"])
print("年龄：", dict1["age"])
dict1["school"] = "清华大学"
print(dict1)

del dict1["name"]
print(dict1)
print(dict1.get("age"))

for item in dict1.items():
    print("key:", item[0], "value:", item[1])

dict2 = {
    "其他信息": {
        "hobby": "足球",
        "company": "xxxx"
    }
}

dict1.update(dict2)

print(dict1)



set_list = [1,1,1,2,3,2,1]
print(set_list)
print(list(set(set_list)))
