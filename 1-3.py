#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 3. 리스트의 합
t = int(input())
for testcase in range(t):
    lst = list(map(int,input().split()))
    sum = 0
    for i in lst:
        sum += i
    print(sum)

