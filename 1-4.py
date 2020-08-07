#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 4. 최댓값과 최솟값의 차
t = int(input())
for testcase in range(t):
    lst = list(map(int,input().split()))
    print(max(lst) - min(lst))


# In[ ]:




