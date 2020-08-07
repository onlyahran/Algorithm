#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 두바퀴 레이스
import collections

t = int(input())
for test_case in range(t):
    car = list(map(int, input().split())) ## 번호는 두번만 나타난다
    q = collections.deque([])
    
    for c in car:
        if len(q) == 0  or q[0] != c:
            q.append(c)
        else:
            q.popleft()
    
    if q:
        print('YES')
    else:
        print('NO')

