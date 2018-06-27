def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i] ,alist[i+1] = alist[i+1] ,alist[i]
                
def select_sort(alist):
    n = len(alist)
    for j in range(n):
        min = alist[j]
        index = j
        for i in range(j+1 ,n):
            if min > alist[i]:
                min = alist[i]
                index = i
        alist[j] ,alist[index] = alist[index] ,alist[j]
        
def insert_sort(alist):
    n = len(alist)
    for j in range(1,n):
        i = j
        while i > 0 and alist[i] < alist[i-1] :
            alist[i],alist[i-1] = alist[i-1],alist[i]
            i -=1
        
def quick_sort(alist ,first ,last):
    low = first
    high = last
    if low >= high -1:
        return 
    mid_value = alist[first]
    while low < high:
        while alist[high] >= mid_value and low < high:
            high -= 1
        alist[low] = alist[high]
            
        while alist[low] <= mid_value and low < high:
            low += 1
        alist[high] = alist[low] 
            
    alist[low] = mid_value    
    quick_sort(alist ,0 ,low-1)
    quick_sort(alist ,low+1 ,last)
    
        
        
if __name__ =='__main__':
    list = [54, 82, 11, 43, 2, 98, 24, 55, 13, 76]
    print(list)
    quick_sort(list ,0 ,len(list)-1)
    print(list)