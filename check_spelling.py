# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:07:56 2016

@author: zhuoli
"""


def check_spelling(city,lenth,let):
    
    letter_space = [0]
    num = 0
    
    for i in range(0,lenth):
        if let == city[i]:
            num = num +1
            letter_space.append(i)
        elif let.upper() == city[i]:
            num = num+1
            letter_space.append(i)
                        
    letter_space[0] = num
    return letter_space
            
            
    

            
        
    
    



