#!/usr/bin/env python
# coding: utf-8

# In[12]:


# priority queue
import heapq

t = int(input())
for _ in range(t):
    n = int(input()) # 명령어 개수
    hq = [] # 빈 큐 선언
    for _ in range(n):
        q = int(input())
        if q == -1:
            if len(hq) != 0:
                min_num = min(hq)
                min_idx = hq.index(min_num)
                print(hq[min_idx])
                heapq.heappop(hq)
        else:
            heapq.heappush(hq, q)

