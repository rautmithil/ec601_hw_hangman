
import random

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
   