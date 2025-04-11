#Remove set items
#To remove an item in a set,
# use the remove(), or the discard() method.
cricketplayer={"tamim","sakib","musfiq","Riyad","mustafiz","sabbir","nasir","mosaddek","alamin","taskin","saif hasan"}
cricketplayer.remove("sakib")
print(cricketplayer)
print('')
#Remove "mustafiz" by using the discard() method:
cricketplayer.discard("mustafiz")
print(cricketplayer)
print("")

#wou can also use the pop() method to remove an item, but this method will remove a random item, 
# so we cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item
x=cricketplayer.pop()
print("remove item:",x)
print(cricketplayer)
print("")

#The clear() method empties the set:
cricketplayer.clear()
print(cricketplayer)