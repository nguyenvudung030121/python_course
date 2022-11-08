# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:18:26 2022

@author: ASUS
"""

# #CACH 1
# letters = ['a', 'b', 'c', 'd']
# print(letters)
# upper_letters = []
# for letter in letters:
#     result = letter.upper()
#     upper_letters.append(result)
# print(upper_letters)



# #CACH 2

# letters = ['a', 'b', 'c', 'd']
# print(letters)
# upper_letters = [x.upper() for x in letters]
# print(upper_letters)

# ------------------------------------------------------
# ages = [1, 34, 5, 7, 3, 57, 356]
# print(ages)
# old_ages = [x for x in ages if x > 10]
# print(old_ages)

# ----------------------------------------------
# ages = [1, 34, 5, 7, 3, 57, 356]
# old_ages = [x for x in ages if x > 10 and x < 100 and x is not None]
# print(old_ages)'

#-----------------------------------------
#BAI TAP 1

# array = [1,2,3,4,5]

# array_add = [(item + 6) for item in array]

# print(array_add)


#-----------------------------------------
#BAI TAP 2

# array2 = [41,51,61,31,71]

# array_add2 = [(item * item) for item in array2 if item > 50]

# print(array_add2)

#-----------------------------------------
#BAI TAP 3

array = ['mango','kiwi','strawberry','guava','pineapple','mandarin orange']



# array_add = [ item for item in array if len(item) > 5]
# array_add = [ item for item in array if 'a' in item]
# array_add = [ item if 'a' in item else item + 'a' for item in array ]
array_add = [ item for item in array if item.count('a') > 1]

print(array_add)



