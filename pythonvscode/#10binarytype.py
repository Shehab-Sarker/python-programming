#Binary type data type bytes,bytearray,memory
#what is bytes in python
#=>the bytes() function returns a byte object
#bytes is immutable it means byte element are not changeable
mylist=[1,2,34,56,78]
bt=bytes(mylist)
print(type(bt))
#byte k convert kora hoy image k compress koraar jonno
"""bitearray
bytearray type is mutubale it means elements are changeable
it is returns a bytearray object,it can convert objects into biytearray objects, 
or create empty bytarray 
object of the specified size. """
mylist2=[12,34,56,78,90]
btary=bytearray(mylist2)
btary[4]=23
print(type(btary))
print(btary[4])
 
 