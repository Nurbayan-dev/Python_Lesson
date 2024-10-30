# Если мы используем print after return - он ре работает
# Есть в городе много регионы,
# в каждом городе есть кафе рестораны, используем dict, list и.т.д.
# - с помощью function должен выходит - рейтинг, средний чек
# кстати - юзер должен мог вести все информации в консоле. если бюджет столько то может пойти туда и покупать то


# def my_function(fname):
#   print(fname + " Refsnes")
#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def say_hello(name):
#     print('Hello', name)
#
# say_hello('Mary')
# say_hello('Tom')

# ---- Мы еще можем создать функцию без значение
# def hello():
#     print('hello')
# hello()


# math ---- summa: 232, umnojit 23232323, delit

# def multiply_numbers(a, b):
#     print ("Умножение", a * b)
# multiply_numbers(5, 7)
#
#
# def add_numbers(a, b):
#     print("Результат 2: ", a + b)
# add_numbers(444, 222)

#
#
# def say_hello(name, name2):
#     print('Hello', name)
#     print('Good bye', name2)
#
# say_hello('Tom', "Mary")
#
#
# def say_hello2(name, name2):
#     print('Hello', name2)
#     print('Good bye', name)
#
# say_hello2('Tom', "Mary")
#
#
# def say_hello(name, name2):
#     print('Hello', name)
#     print('Good bye', name2)
#
# say_hello(name2 = 'Tom', name = "Mary")


#
# def sumFun(num1, num2):
#     sum1 = num1 + num2
#     # print(sum1)
#     return sum1
# sum_result = sumFun(2,5)
# print(sum_result)


# def sumFun(num1, num2):
#     sum1 = num1 + num2
#     # print(sum1)
#     return sum1

# sum_result = sumFun(2,5)
# print(sum_result)


# def multiply(result, num3):
#     mul = result * num3
#     return mul
#
# result = sumFun(6, 2)
#
# final = multiply(result, 4)




# number2 = sum_result * 2
# print(number2)

# result = sumFun(6, 2)





# def multiply(result, num3):
#     mul = result * num3
#     return mul


# - - - -  - - - - - - - - - - - - - - - - - - - - - -- -


restaurants = {
    "Центральный": [
        {"Supara": "Cafe Central", "рейтинг": 4.5, "средний_чек": 20},
        {"Navat": "Gourmet Bistro", "рейтинг": 4.7, "средний_чек": 35},
    ],
    "Северный": [
        {"Zerno": "North Eatery", "рейтинг": 4.2, "средний_чек": 15},
        {"Usta Turkish Restaurant": "Highland Grill", "рейтинг": 4.9, "средний_чек": 50},
    ],
    "Южный": [
        {"Eki dos": "Fast food", "рейтинг": 4.0, "средний_чек": 10},
        {"DoDO": "Pizza", "рейтинг": 4.8, "средний_чек": 30},
    ]
}

region_input = "Центральный"
budget_input = 30
min_rating_input = 4.0

