## playing with Library function
a = 6
b = 5
# c = sum(a, b) #sum function takes list or tuple (iterable)
c = sum ([a, b]) #sum with LIST
print(c)
d = sum ((a,b)) #sum with TUPLE
print(d)
e = sum({a,b}) #sum with SET
print(e)

f = sum({a:b})
print(type(f))
print(f) #when we iterate, DICT only give us the KEYS. so it will print 6



## playing with user defined function
def average1(a, b): #don't have to use the return type
    """This function will return the average of two numbers""" #function's documentation is in here
    c = a+b
    return c/2


## Trying to overLoad function
## Python don't support function overLoading
## by default Python consider the last function as only implementation
def average1(iterable):
    a = sum(iterable)
    b = len(iterable)
    return a/b

print(average1({3, 3}))
print(average1.__doc__)  #printing the written documentation
print(average1([3, 2, 3, 1])) 




