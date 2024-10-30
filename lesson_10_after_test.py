# 10.10.24.
from aiofiles.os import remove

# numbers1 = [1,2,3,4,5]
# numbers2 = numbers1            # numbers2 ичин өзгөртсө numbers1 да өзгөрөт. Присваивание
                                    # numbers1 == numbers2
# print(numbers2)
#
# numbers2.append(100)
# print(numbers1)
# print(numbers2)
#
# numbers1[2] = 200
# print(numbers1)
# print(numbers2)

# - - - - - - - - - - - - - - - - - - -

# year1 = ['A', 'B', 'C', 'D', 'E', 'F']
# year2 = year1.copy()                  #  year1 != year2
# year1[1] = 'BBB'
# year1.insert(0, 400)
# print(year1)


# - - - - ->  Удалить  <- - - -
# people = ["Make", "Anna", "Tom", "Sam"]
# del people[1]
# print(people)
#
# people.remove('Tom')
# print(people)
#
# people.clear()
# print(people)

#  - - - - ->  Добавить  <- - - -
# append, insert, index, extend

# people = ["Make", "Anna", "Tom", "Sam"]
#
# people.append("Alice")
# people.insert(1, "Bill")
# people.extend(["Mike", "Sam"])


# a = []
# b = ()
# print(type(b))
# print(type(a))





# - - - - - - - - - - - - - - - - - - list comprehension
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# positive_numbers = []
# for n in numbers:
#     if n > 0:
#         positive_numbers.append(n)
# print(positive_numbers)  # [1, 2, 3]



# [expression for item in iterable (if condition)]
# positive_numbers2 = [n for n in numbers if n > 0]
# print(positive_numbers2)

# умножить на 2





