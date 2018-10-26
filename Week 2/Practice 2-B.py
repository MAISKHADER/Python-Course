#!/usr/bin/env python
# coding: utf-8

# In[5]:


cur1 = str(input ("Choose one of these currencies (JOD, TL, USD) to convert from"))
cur2 = str(input ("Choose one of these currencies (JOD, TL, USD) to convert from"))
amount =float(input ("input the amount to convert = " ))

if cur1 == "JOD" and cur2 == "TL":
              
    amount = float(amount)*7.86
    print (amount)
              
elif cur1 == "TL" and cur2 == "JOD":
    
    amount = float(amount)*0.13
    print (amount)

elif cur1 == "USD" and cur2 == "TL":
    
    amount = float(amount)*5.58
    print (amount)

elif cur1 == "TL" and cur2 == "USD":
    
    amount = float(amount)*.18
    print (amount)
    
elif cur1 == "JOD" and cur2 == "USD":
    
    amount = float(amount)*1.41
    print (amount)
    
elif cur1 == "USD" and cur2 == "JOD":
    
    amount = float(amount)*0.71
    print (amount)
    
              
    


# In[ ]:




