#!/usr/bin/env python
# coding: utf-8

# # Welcome to the first Python workshop

# In[2]:


1+2


# In[1]:


2*3


# In[4]:


1+1
2+2
3+4


# In[ ]:


7/2


# In[5]:


3**7


# In[6]:


7-3


# In[7]:


print(x)


# In[ ]:


x=7


# In[9]:


x


# In[16]:


print(x)


# In[10]:


x=7


# In[11]:


x


# In[12]:


print(x)


# In[13]:


x-x+1


# In[14]:


x+x+1


# In[15]:


x*x+1


# In[17]:


x +-3


# In[18]:


x


# In[19]:


x +- 3


# In[20]:


x=x+1


# In[21]:


x=7


# In[22]:


x=x+1


# In[23]:


print(x)


# In[54]:


y=7


# In[55]:


x+y


# In[26]:


y=7


# In[27]:


print(y)


# In[28]:


x+y


# In[29]:


type(x)


# In[30]:


type(y)


# In[31]:


s= 'hello'


# In[32]:


s


# In[35]:


t="hello"


# In[36]:


s="ll"


# In[37]:


print(s)


# In[38]:


print(t)


# In[40]:


s[1]


# In[ ]:





# In[44]:


s [2]


# In[45]:


s[-1]


# In[47]:


s[-2]


# In[48]:


s[:10]


# In[49]:


s[5:]


# In[50]:


s[5:18:2]


# In[51]:


print(s)


# In[62]:


k = [1,2,3]


# In[63]:


k


# In[64]:


k[0]


# In[65]:


k[-1]


# In[66]:


k[:2]


# In[77]:


m = [1,"fred", True, 3.14]


# In[78]:


m


# In[70]:


s[5] = I


# In[73]:


s[1]


# In[79]:


m[1] = 99


# In[80]:


m


# In[81]:


m[:3]


# In[83]:


m[:3] = [1,2,3]


# In[84]:


m


# In[85]:


m + [1,2,[3,4], m]


# In[87]:


p = (1,2,3,4,5)


# In[88]:


p


# In[89]:


p[2] = 99


# In[103]:


# Dictionaries


# In[106]:


mydict = {'First name': 'Tari', 'Last name': 'Lake', 'room': 202}


# In[107]:


mydict


# In[117]:


mydict['First name']


# In[118]:


mydict['room']


# In[119]:


mydict['sandwiches'] = ['cheese', 'egg maiyonnaise', 'ham']


# In[120]:


mydict


# In[121]:


mydict['sandwiches']


# In[122]:


mydict['sandwiches'][1]


# In[123]:


#Flow control


# In[124]:


x = [1,2,3,4,5,6,]


# In[125]:


x


# In[126]:


for item in x:
    print(item*2)
    print(item*3)
    
    print("they're different")
    
    print("I'm now outside the loop")


# In[129]:


print(item*6)


# In[130]:


for item in x:
    print(item*1)
    
    print("I'm tari")
    print("What time is lunch?")
   
    print(item*5)
    print(item*6)
    print("I guess we're waiting" )


# In[132]:


for item in range(6):
    print("item is", item)


# In[133]:


help(range)


# In[134]:


for item in range(1,10,2):
    print(item)


# In[135]:


for item in range(10,1,-1):
    print("item is", item)


# In[136]:


mydict


# In[137]:


for item in mydict:
    print(item)


# In[138]:


mydict.keys()


# In[139]:


mydict.values()


# In[140]:


mydict.items()


# In[142]:


for item in mydict.values():
    print(item)


# In[156]:


for items in mydict.items():
    print(item)


# In[157]:


for item in mydict.items():
    print("key is ,item[0], "value is":item[1])


# In[147]:


a,b = 7,9

print(a)
print(b)


# In[148]:


a,b = b,a

print(a)
print(b)


# In[151]:


for key,value in mydict.items():
    print("key is>>>"), key, "<<< value is>>>", value, "<<<"


# In[158]:


#While Loops


# In[159]:


x


# In[162]:


i = 0

while i < 4:
    print(i)
    i += 1


# In[ ]:


S = 4

difference = 1000

guess = 3

while difference > 0.001:
    new_guess = (guess + S/guess)/2
    difference = abs(new_guess-guess)
    guess = new_guess
    print(guess, difference)


# In[ ]:




