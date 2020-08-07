#!/usr/bin/env python
# coding: utf-8

# In[12]:


# queue
import collections

t = int(input())
for _ in range(t):
    n = int(input()) # 명령어 개수
    queue = collections.deque([]) # 빈 큐 선언
    for _ in range(n):
        q = int(input())
        if q == -1:
            if len(queue) != 0:
                print(queue[0])
                queue.popleft()
        elif q > 0:
            queue.append(q)
        else:
            continue

