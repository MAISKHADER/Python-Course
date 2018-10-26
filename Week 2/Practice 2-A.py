#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_prime_numbers (n):
    n = input ("How many prime numbers to print?  ")
    x=0   
    while int(x)<int(n) :
        for i in range (2,x):
            if int(x)%i == 0:
                print (x)
                x=x+1
            else: 
                x=x+1
        break
        
        
print (print_prime_numbers(1))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




