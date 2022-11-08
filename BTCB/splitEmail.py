# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:21:28 2022

@author: ASUS
"""

def splitEmail(arrEmail,st):
    st_split = st.split(" ") 
    for item in st_split:
        if '@' in item :
            arrEmail.append(item)
            
def splitDateTime(arrDateTime,st):
    index_symbol = st.find('@')
    index_space = st.find(" ",index_symbol)
    st_time = st[index_space+1:]
    arrDateTime.append(st_time)


f = open("emails.txt", "r")
arrEmail,arrDateTime = [],[]
data = f.readlines()
for st in data :
    if ('From ' in st):
        splitEmail(arrEmail, st)
        splitDateTime(arrDateTime, st)
    