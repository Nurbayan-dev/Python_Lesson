# 15.10.24. lesson
from Tools.scripts.make_ctype import values

# Словарь (dictionary)

# users = {1: "Tom", 2: "Bob", 3: "Bill"}

# score = {
#     'Alihan': 40,
#     'Asel': 40,
#     'Nurbayan': 10
# }

# objects = {1: "Tom", "2": True, 3: 100.6}


# group = {
#     'Nurbayan': 'CS-31',
#     'Asel': 'CS-41',
#     'Adelina': 'CS-32',
#     'Erkin': 'CS-24',
#     'Kamila': 'CS-25'
# }

# print(group['Arsen'])              # Error
# group['Arsen']  = 'CS-32'
# print(group)

# group['Asel']  = 'CS-444'
# print(group)

# print(group)
# print(group['Nurbayan'])



users = {
    "+11": "Tom",
    76: 'me',
    56.7:'you',
    "+33": "Bob",
    "+55": "Alice",
    3: ['Mary', 24, 67, 66],
    65: ['Jeff', 44, 55, 66]
}

# key_list = []
# value_tuple = ()
# sameValue = 0
# value_list = []
#
# for key, value in users.items():
#     key_list.append(key)
#     value_list.append(value)
# print(key_list)
#
# value_tuple = tuple(value_list)
# print(value_tuple)


# key_list = list(users.keys())
# print(key_list)
# print(type(key_list))


# value_tuple = tuple(users.values())
# print(value_tuple)

# if key_list = value_tuple:

#     print()
# sameValue = key_list == value_tuple
# print(sameValue)

# for i in users:
#     print(i)
#
# for key in users.keys():
#     print(key)
#
# for value in users.values():
#     print(value)


# for key, value in users.items():
#     print(key)
#     print(value)


# for key, value in users.items():
#     if key == 3:
#         print(value)


# newUsers = {3: ['Mary', 24, 67, 66], 65: ['Jeff', 44, 55, 66]}
# newUsers.update(users)
# print(newUsers)

# user1 = users.get("+55")
# print(user1)  # Alice
# user2 = users.get("+33", "Unknown user")
# print(user2)  # Bob
# user3 = users.get("+44", "Unknown user")
# print(user3)  # Unknown user

# del users['+11']
# print(users)
# deletedInfo = users.pop('+36', 'there is no this key')           # удаляет элемент по ключу key и возвращает удаленный элемент
# print(deletedInfo)

# users.clear()
# print(users)



# student = users.copy()
# print(student)


#  - - - --  - - - - - - - - - - - - - - -- - - - - ---  -

# HW - Work with dict in dict. Methods of getting key or value into dict...
#
# people = {'person1': {
#     'Maried': True,
#     'Salary': 23000
#     },
#
#     'person2': {
#     'Maried': True,
#     'Salary': 23000}
#         }

# people['person1']['Age'] = 30

# people['person3'] = {
#     'Maried': False,
#     'Salary': 18000,
#     'Age': 25
# }
#
# print(people)


# del people ['person1']
# print(people)
#
# del people ['person1']['Maried']
# print(people)

# print(people.pop('person1'))
# print(people.pop('person2'))
#
# people.clear()

# print(dict1['person1']['Maried'])

# new_list_from_dict = list(people.values())
# print(new_list_from_dict)





# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#
# people[3] = {}
#
# people[3]['name'] = 'Luna'
# people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'
#
# print(people[3])


# - - - - -  - - - - -повторение - - - -
# list1 = [1, 4.2, 'fads', 222]
# list2 = list(1,2,3,4)
# print(list2)

# word_dict = {'apple': "яблоко", "water": "вода"}
# word_dict1 = dict("apple": "яблоко", "water": 'вода')



# my_tuple = (('student', 'Mike'),
#             ('student2', 'Tom'),
#             ('student3', 'Sam'),)

# my_dict = dict(my_tuple)
# print(my_dict)

