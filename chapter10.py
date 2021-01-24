# 读取整个文件（目录中有pi_digits.txt文件）
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#file_path = 'C:\Users\32671\PycharmProjects\pythonProject\tuling\pi_digits.txt'  #绝对路径
#with open(file_path) as file_object:
#   contents = file_object.read()
#  print(contents.rstrip())
#在Linux和OS X中，使用/而不是\

#逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()   #readline()不一样

for line in lines:
    print(line.rstrip())

#使用文件的内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#包含一百万位的大型文件
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

#圆周率中包含你的生日吗
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

#写入空文件
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

#读取模式（'r'）
#写入模式（'w'）
#附加模式（'a'）
#读取和写入文件的模式（'r+'）
#如果省略了模式实参，Python将以默认的只读模式打开文件

#写入多行
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#附加到文件:给文件添加内容，而不是覆盖原有的内容
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also lve finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

#使用多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

#失败时一声不吭
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass   #修改部分
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

#使用json.dump()和json.load()存储数据
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

import json

filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)

#保存和读取用户生成的数据
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("We'll remember you when you come back, " + username + "!")

import json

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

#重构
import json

def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()

import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename =  'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back, " + username + "!")

greet_user()


import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()