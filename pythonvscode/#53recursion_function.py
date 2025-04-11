#Increasing the recursion limit : Python has default maximum recursion depth of 1000.
#if a function exceeds tis limit. it can be incrreased using the sys.setrecursionlimit(n) function
# def refun():
#     print("hablu")
#     refun()
    
# refun() 
# print('')

"""Recursion
Python also accepts function recursion,
which means a defined function can call itself.
Recursion is a common mathematical and programming concept.
It means that a function calls itself. This has the benefit of meaning that
wecan loop through data to reach a result.
The developer should be very careful with
recursion as it can be quite easy to slip into
writing a function which never terminates, or one that uses excess amounts of memory or
processor power. However, when written correctly recursion can be a very efficient and
mathematically-elegant approach to programming."""   
def tri_recursion(k):
    if(k>0):
        res=k+tri_recursion(k-1)
        print(res)
        return res
    else:
        return 0   
print("Recursion example result")
print(tri_recursion(6))