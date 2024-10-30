# 11.10.24.
# List comprehension
# example циклы - 1)for      2) for + List comprehension   3)while     4) while + List comprehension
from copyreg import pickle

#  - - - - - - -  1)for  - - - - - - - - - -
# numbers = [1, 2, 3, 4, 5]
#
# for number in numbers:
#     print(number)

#
# for i in range(10):
#     if i % 2 == 0:
#         print(i)

# - - - - - - - - - 2) for + List comprehension - - - - - -
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)



# - - - - - - - - - - 3)while  - - - - - - - - - - - -

# numbers = [0, 5, 10, 6, 3]
# length_num = len(numbers)
# n = 0
# while n < length_num:
#     print(numbers)
#     n += 1







# если число + позитивные тогда код должен сделать его в 3(кубе) если - негативные число тогда он выводит само число


# numbers = [1, -2, 3, -4, 5]
#
# result= [num ** 3 if num > 0 else num**2 for num in numbers]
#
# print(result)







