from functools import wraps
import datetime

def intime(f):
    @wraps(f)
    def inner_wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        res = f(*args,**kwargs)
        end = datetime.datetime.now()
        print(f"runtime = {(end-start).total_seconds()}")
        return res
    return inner_wrapper

@intime
def insertion_sort(arr):
    for i in range(1,len(arr)):
        # Grab pivot element
        pivot = arr[i]
        # Sort from pivot till index 0
        j = i-1
        while(j>=0 and arr[j] > pivot):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = pivot
    return arr
