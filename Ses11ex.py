#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:11:06 2018

@author: Julie
"""

#%%

prices = {'Guitar': 1000, 
          'Pick box': 5, 
          'Guitar Strings': 10
          }

cart= ['Guitar', 'Pick box']
cart2= ['Guitar','Guitar', 'Pick box']

prices_in_cart = []

def checkout_white(shoppingcart_list):
    prices_in_cart.clear()
    if len(shoppingcart_list) == 0:
        return 'Your shopping cart is empty.'
    else: 
        for i in shoppingcart_list:
#            print(i)
            prices_in_cart.append(prices[i])
        return sum(prices_in_cart)

#%%
            

prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}

cart3 = ["Guitar","Guitar Strings","Guitar Strings","Guitar"]
cart4 = ["Pick Box", "Guitar","Insurance","Insurance", "Priority mail", "Priority mail"]
cart = ["Guitar"]

prices_in_cart = []

def checkout_blue(shoppingcart_list):
    prices_in_cart = []
    
    
    if "Insurance" in shoppingcart_list:
            prices_in_cart.append(prices["Insurance"])
            
    for i in shoppingcart_list:
    
        if "Insurance" in shoppingcart_list:
            
            shoppingcart_list.pop(shoppingcart_list.index("Insurance"))
            
           # print(shoppingcart_list)
            
    if "Priority mail" in shoppingcart_list:
            prices_in_cart.append(prices["Priority mail"])
            
    for i in shoppingcart_list:
    
        if "Priority mail" in shoppingcart_list:
            
            shoppingcart_list.pop(shoppingcart_list.index("Priority mail"))
            
            # print(shoppingcart_list)
        
    if shoppingcart_list == []:
        return 'Your shopping cart is empty.'
    
    else:
        
        for i in shoppingcart_list: 

            prices_in_cart.append(prices[i])
            
            # print(prices_in_cart)
                
    return sum(prices_in_cart)

#%% PROBLEM, ALSO NO DOUBLE GUITAR
prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}
prices_in_cart = []
new_cart = []
trash = []


def checkout_blue2(shoppingcart_list):
    
    for x in shoppingcart_list:
        if x not in new_cart:
            new_cart.append(x)
        else:
            trash.append(x)
      
    
    
    if shoppingcart_list == []:
        return 'Your shopping cart is empty.'
    
    else:
        
        for i in new_cart: 

            prices_in_cart.append(prices[i])
            
            print(prices_in_cart)
            print(new_cart)
            print(trash)
                
    return sum(prices_in_cart)

#%% BLACKKKKKK
            

prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}


prices_in_cart = []

silver_check = []

def checkout_black(shoppingcart_list, tier):
    prices_in_cart = []
    
    
    if "Insurance" in shoppingcart_list:
            prices_in_cart.append(prices["Insurance"])
            silver_check.append('Insurance')
            
    for i in shoppingcart_list:
    
        if "Insurance" in shoppingcart_list:
            
            shoppingcart_list.pop(shoppingcart_list.index("Insurance"))
            
           # print(shoppingcart_list)
            
    if "Priority mail" in shoppingcart_list:
            prices_in_cart.append(prices["Priority mail"])
            silver_check.append('Priority mail')
            
    for i in shoppingcart_list:
    
        if "Priority mail" in shoppingcart_list:
            
            shoppingcart_list.pop(shoppingcart_list.index("Priority mail"))
            
            # print(shoppingcart_list)
        
    if shoppingcart_list == []:
        return 'Your shopping cart is empty.'
    
    else:
        
        for i in shoppingcart_list: 

            prices_in_cart.append(prices[i])
            
            # print(prices_in_cart)
                
    if tier == 'silver':
        if "Insurance" in silver_check:
            return ((sum(prices_in_cart) - 5)*0.98) + 5
        if "Priority mail" in silver_check:
            return ((sum(prices_in_cart) - 10)*0.98) + 10
    
    if tier == 'gold':
        return (sum(prices_in_cart))*0.95
    elif tier == 'normal':
        return sum(prices_in_cart)

