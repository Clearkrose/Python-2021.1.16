magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:   #不要遗漏冒号
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")   #缩进代表在循环里，这里不能缩进

print("Thank you, everyone. That was a great magic show!")

#使用函数range()
for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

#使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))   #最后一个数字是步长
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

squares = [value**2 for value in range(1,11)]   #列表解析
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#遍历切片
players = ['charles', 'martina', 'michael', 'folrence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]   #friend_foods = my_foods行不通

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are;")
print(friend_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])   #dimensions[0] = 250无效，试图修改元组的操作是被禁止的。

#遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#修改元组的变量
dimensions = (200, 50)
print("Original dimension:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)