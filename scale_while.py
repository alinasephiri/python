'''
takes in a list and a number but does not return anything.
Modify each element of the list by multiplying it by value.
You must use a while loop.
'''
def scale_while(alist,value):
    # position of the element in the list
    idx = 0
    while idx < len(alist):
        # multiply the element by the given value
        alist[idx] = alist[idx] * value
        idx += 1
