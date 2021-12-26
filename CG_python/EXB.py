import numpy as np
def unfold_with_overlap(x):
    new_list=[]
    length=len(x)-1
    last = x[length][-2:]
    new_list = np.delete(x, [-2,-1], 1)
    result = np.append(np.ravel(new_list),last)
    return result
    
a = np.array(
    [ [0, 1, 2, 3],
      [2, 3, 4, 5],
      [4, 5, 6, 7] ])
c = np.array([
    [0,1,2,3,4,5,6],
    [5,6,7,8,9,10,11],
    [10,11,12,13,14,15,16],
    [15,16,17,18,19,20,21]
])
d = np.array([
    [0,1,2,3,4,5],
    [4,5,6,7,8,9]
])
b = unfold_with_overlap(d)
print(b)