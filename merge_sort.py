#author 比嘉信斗　185715B

import time
import random
import os
import concurrent.futures 

#統合部
def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    for i in range(left,right):
        if len(L) == 0:
            A[i] = R.pop(0)
        elif len(R) == 0:
            A[i] = L.pop(0)
        elif L[0] <= R[0]:
            A[i] = L.pop(0)
        else:
            A[i] = R.pop(0)

#分割部
def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        mergesort(A, left, mid)
        mergesort(A, mid,right)
        merge(A, left, mid, right)     

width = 1000000
divide = 4
period = int(width/divide)
A = [a+1 for a in range(width)]
random.shuffle(A)
# os.cpu_count() == 4


#通常実装する場合のmergesort()
for c in range(divide):
    #print("["+str(period*c)+","+str(period*(c+1))+"]")
    mergesort(A,period*c,period*(c+1))



#並列処理を適応する場合のmergesort()

"""
if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)    
    for p in range(divide):
        executor.submit(mergesort(A,period*p,period*(p+1)))
"""
    
