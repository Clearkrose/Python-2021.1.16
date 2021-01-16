print("Hello Python world!")

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

#变量名只能包含字母、数字和下划线。
#变量名可以字母或下划线打头，但不能以数字打头。
#变量名不能包含空格
#不要将Python关键字和函数名用作变量名
#变量名应既简短又有描述性
#慎用小写字母l和大写字母O

mesage = "Hello Python Crash Course reader!"
print(mesage)

#字符串
"this is a string"
'this is also a string'
'I told my friend, "Python is my favourite language!"'
"The language 'Python' is named agter Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favourite_language = 'python '
print(favourite_language)
print(favourite_language.rstrip())
print(favourite_language)

favourite_language = ' python '
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

print( 2 + 3 )
print( 3 - 2 )
print( 2 * 3 )
print( 3 / 2 )
print( 3 ** 2 )
print( ( 2 + 3 ) * 4 )

#浮点数
print( 0.1 + 0.1 )
print( 2 * 0.1 )
print( 0.2 + 0.1 )
print( 3 * 0.1 )

#str()：将数值23转换为字符串
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)