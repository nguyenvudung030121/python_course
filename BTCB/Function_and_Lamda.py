# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:18:58 2022

@author: ASUS
"""
# ---------------------------------- HÀM CÓ SẴN ----------------------------
#Hàm Filter lấy ra những giá trị ở sequence 
#đem so sánh trong func trả về list giá trị nếu true

# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# # using filter function
# filtered = list(filter(fun, sequence))
# print(filtered)


# #Hàm Map nhanh hơn for
# # Return double of n
# def addition(n):
#     return n + n
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))


# ---------------------------------- TẠO HÀM ----------------------------
# 1. Function: Ham Co ten
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay." )
#     print('I sleep all night and I work all day.' )
# 2. Lambda Ham Khong ten
    # Một hàm Lambda trong Python có cú pháp sau:
    # lambda tham_so: bieu_thuc
    
# nhan_doi = lambda a: a * 2
# print(nhan_doi(10))

# # 3. Lambda ket hop filter
# list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
# list_moi = list(filter(lambda a: (a%2 == 0) , list_goc))
# print(list_moi)

# #4. Sau đây là ví dụ về hàm lambda với hàm map().
# list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
# list_moi = list(map(lambda a: a*2 , list_goc))
# print(list_moi)

# ------------IN HOA TAT CA KY TU TRONG CHUOI----------------
# list_char = ['a','b','c','d','e']

# list_charUpper = list(map(lambda a: a.upper(),list_char))
# print(list_charUpper)

#-----------Tìm và Đếm số Nguyên tố trong khoảng-------------

def check_prime(x):
    if x <= 1 :
        return False
    elif x==2:
        return True
    elif (x % 2 == 0):
        return False
    else:
        for i in range(3,x,2):
            if x % i == 0:
                return False
    return True


print( "Danh sach so NT: ",end = " ")
[print(number,end=" ") for number in range(1,101) if check_prime(number)]


















