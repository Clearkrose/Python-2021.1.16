cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#检查是否相等
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')
print(car == 'Bmw')   #两个大小写不同的值会被认为不相等

car = 'Audi'
print(car.lower() == 'audi')
print(car)

#检查是否不相等
requested_topping = 'mushrooms'

if requested_topping != 'anchobies':
    print("Hold the anchobies!")

age = 18
print(age == 18)

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#使用and检查多个条件：如果每个测试都通过了，真个表达式就为True；如果至少有一个测试没有通过，整个表达式就为False
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

#使用or检查多个条件，只要至少有一个满足，就能通过整个测试
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#要判断特定的值是否已包含在列表中，可使用关键字in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a reponse if you wish.")

#条件测试
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")    #缩进

#if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Habe you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please fegister to vote as soon as you turn 18!")

#if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

#使用多个elif代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price - 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

#省略else代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

#测试多个条件
requested_toppings = ['mushirooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushroom.")
if 'prpperoni' in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese']

#如果这样写，就达不到上面的效果
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza.!")

#检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")