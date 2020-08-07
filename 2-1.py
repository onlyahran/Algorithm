#!/usr/bin/env python
# coding: utf-8

# In[12]:


# stack

t = int(input())
for _ in range(t):
    n = int(input()) # 명령어 개수
    stack = []
    for i in range(n):
        q = int(input())
        if q == -1:
            if len(stack) != 0:
                print(stack[len(stack)-1])
                stack.pop()
        elif q > 0:
            stack.append(q)
        else:
            continue


# In[ ]:




