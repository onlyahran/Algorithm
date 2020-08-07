#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 6. 탐색
t = int(input())
for testcase in range(t):
    lst1 = list(map(int,input().split()))
    lst2 = list(map(int,input().split()))
    ans = []
    for i in lst2:
        if i in lst1:
            ans.append("YES")
        else:
            ans.append("NO")
    print(*ans)

