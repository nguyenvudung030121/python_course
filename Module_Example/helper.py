# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:07:16 2022

@author: ASUS
"""

def n_max_number(n, k=2):
    n.sort()
    list_n_max_number = n[-k:]
    return list_n_max_number