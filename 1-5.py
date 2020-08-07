#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 5. 정렬
t = int(input())
for testcase in range(t):
    lst = list(map(int,input().split()))
    lst.sort(reverse = True)
    print(*lst)


# In[ ]:




