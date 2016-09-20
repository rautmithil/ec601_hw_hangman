# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:57:21 2016

@author: zhuoli, mithil
"""

import pandas
import random
data = pandas.read_csv('macities.csv')


board = [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]

def drawh(i):
    print(board[i])
    
def count_ch(i):
    ch = 6 #Maximum chances are 6
    rem=ch-i
    print ('Chances remaining: ',rem)

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
    

def print_puzzle(city,num_let):
    city_str = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if num_let <= 5:
        
        
        
        bit_0 = random.randint(1,num_let)
                
        
        for i2 in range(0,num_let):
            city_str[i2] = city[i2]
            
        for j in range(0,bit_0):
            city_str[j] = '_'
            
        for j2 in range(bit_0+1,num_let):
            city_str[j2] = '_'
            
            
        #city_print = "".join(city_str)
        for k in range(0,num_let):
            print(city_str[k],' ', end ='')
        
    else:
            
        #checking if there is a space in the city name
        space = ' '
        seq = range(num_let+1)
        
        space_alarm = 0
        
        for i1 in city:
            if i1 == ' ':
                space_alarm = 1
                
        
        #randomly decide tow letters to be remianed
        if space_alarm == 1:
            space_bit = city.index(space)
            bit_1 = random.randint(0,space_bit-1)
            bit_2 = random.randint(space_bit+1, num_let-1)
            
            if bit_1 > bit_2:
                temp_tran = bit_1
                bit_1 = bit_2
                bit_2 = temp_tran
        
            
            #replace other letters with _
            for i2 in range(0,num_let):
                city_str[i2] = city[i2]
                
            for j in range(0,bit_1):
                city_str[j] = '_'
                
            for j2 in range(bit_1+1,space_bit):
                city_str[j2] = '_'
                
            for j3 in range(space_bit+1,bit_2):
                city_str[j3] = '_'
            
            for j4 in range(bit_2+1, num_let):
                city_str[j4] = '_'
                
            #city_print = "".join(city_str)
            for k in range(0,num_let):
                print(city_str[k],' ', end ='')
                
        else:
            bit_12 = random.sample(seq,2)
            bit_1 = bit_12[0]
            bit_2 = bit_12[1]
        
            if bit_1 > bit_2:
                temp_tran = bit_1
                bit_1 = bit_2
                bit_2 = temp_tran
                #print(bit_12)
            
            
            
            for i2 in range(0,num_let):
                city_str[i2] = city[i2]
                
            for j in range(0,bit_1):
                city_str[j] = '_'
                
            for j2 in range(bit_1+1,bit_2):
                city_str[j2] = '_'
                
            for j3 in range(bit_2+1, num_let):
                city_str[j3] = '_'
                
            #city_print = "".join(city_str)
            for k in range(0,num_let):
                print(city_str[k],' ', end ='')
                
        return city_str
        
    
#using data.city[i] to read the i city
#print(data.city)

#pick up a city randomly
sel_city = random.randint(1,473)
#print (sel_city)
sel_city = 350

city = data.city[sel_city]
#print(city)

#count the amount of letters
num_let = len(city)
#print (num_let)
print('Welcome to hangman')
drawh(0)
print('This is the name of a city in MA')     

city_str = print_puzzle(city,num_let)       
incorrect = 0
used_letter = []

print('\nPlease geuss a letter:')

while(True):
            

    letter = input()
    sign = check_spelling(city,num_let,letter)
    if sign[0] == 0:
        incorrect = incorrect + 1
        if incorrect < 6:
            print ('This letter is not contained in the city name')
            used_letter.append(letter)
            drawh(incorrect)
            count_ch(6-incorrect)
            print ("Letter used: ",used_letter)
            for k2 in range(0,num_let):
                print (city_str[k2],' ', end ='')
            print('Please geuss a letter:')
        else:
            print ('This letter is not contained in the city name')
            drawh(6)
            print ('Game Over')
            break
    else:
        for nn in range(0,sign[0]):
            city_str[sign[nn+1]] = letter
        print ('That is a correct letter')
        for k3 in range(0,num_let):
            print (city_str[k3],' ', end ='')


        flag = 1
        
        for k2 in range(0,num_let):
            if city_str[k2] == '_':
                flag = 0;

                
        if flag == 1:
            print ('\nWell Done')
            break
        else:
            print('\nPlease geuss a letter:')
            
            