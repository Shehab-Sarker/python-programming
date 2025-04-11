#Add items in python
"""Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method."""
thisset={"shehab","sarker","Rifat","Rahim"}
thisset.add("karim")
print(thisset)
print("")

#ADD Sets
#To add items from another set into
# the current set, use the update() method.
tropical=("apple","banana","cherry")
thisset.update(tropical)
print(thisset)
print('')

#Add any Iterable
#The object in the update() method does not have to be a set, it can be any iterable
# object (tuples, lists, dictionaries etc.).
mylist=["shahabuddu","chuppu",1,56,6987]
thisset.update(mylist)
print(thisset)
print('')