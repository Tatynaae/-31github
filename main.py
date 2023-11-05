# print("Hello")
# comment
# print(10/2)
# print(10//2)
# print(10 * 2)
# print(10 ** 2)
# print(10 % 3)
# print(min(1, 2, 3, 4, -3, -5))
# print(max(1, 2, 3, 4, -3, -5))
# print(abs(-100))
# print(pow(2, 2))
# print(round(5 / 3))
#
# input("Print your age: ")
#
# print("result:", 10, 12, sep="/", end="!\n")
# print("second \" \\ line")
# print("second \" \t line")
#
# variables
#
# number = 5
# print(number)
#
# number = 3
# del number
# print(number)
#
# number = 7
# print(number)
#
# digit = 3
# word = "result:"
# some_num = "4"
# print(word, digit)
# print(word + str(digit))
# print(digit + int(some_num))
#
# boolean = True | False
# booleans = True & False
# print(boolean)
#
# num1 = int(input("Write first integer:"))
# num2 = int(input("Write second integer:"))
#
# print("Result:", num1 + num2)
# print("Result:", num1 - num2)
# print("Result:", num1 * num2)
# print("Result:", num1 / num2)
# print("Result:", num1 ** num2)
# print("Result:", num1 // num2)
# num1 += 3
# print("result:", num1)
# print("Result:", int(num1) + int(num2))
#
# word = "Hi"
# print(word * 3)
#
#
#  Условные операторы:
# if 5 == 5:
#     print("Yes")
#     print("!!!")
#
# user_data = int(input("Write an integer:"))
# if user_data == 5:
#     print("Number is bigger than 5!")
# elif user_data == 100:
#     print("Is it 100?")
# else:
#     print("NOO!!")
#
# isHappy = False
# isHappy = True
# if isHappy:
#     print("User is Happy!")
# else:
#     print("User is not Happy!")
#
# if not isHappy:
#     print("User is not Happy!")
#
# "AND" === "&&"
# if user_data == 10 and isHappy:
#     print("Awesome!")
# else:
#     print("So pity!")
#
# "OR" === "||"
# if user_data == 10 or isHappy:
#     print("Awesome!")
# else:
#     print("So pity!")
#
# Тернарный оператор:
data = input()

number = 5 if data == "Five" else 0

if data == "Five":
    number = 5
else:
    number = 0

print(number)
