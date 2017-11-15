'''
Created on 15.11.2017

@author: sabrinahiestand
'''
import numpy as np
import pandas as pd

# def test_run():
#     print (np.array([(2, 3, 4), (5,6,7)]))
#     print (np.ones((5,4,3), dtype=np.int_))
#     np.random.seed(693)
#     pd = np.random.randint(0, 10, size=(5,4))
#     print ("Array:\n",pd) 
#     print ("Min:\n", pd.min(axis=0))
#     print (len(pd.shape))
#     print (pd.dtype)
#     print (pd)
# #     pd.plot()
    
def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    # TODO: Your code here
    print ("Max in a: ", a.max())
    return a.argmax()


def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print ("Array:", a)
    
    # Find the maximum and its index in array
    print ("Maximum value:", a.max())
    print ("Index of max.:", get_max_index(a))
    print ("Element 4: ",a[3])
    indices = np.array([1,1,2,3])
    print (a[indices])
    print (a*a)

if __name__ == "__main__":
    test_run()
    
if __name__ == "__main__":
    test_run()
    