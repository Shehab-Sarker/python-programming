#Remove items from the list
#The remove() method removes the specified item
playlist=["Messi","Ronaldo","Mbappe","Neymer","Holand","Martinez","Dimaria","Maradona","Pele","Suarez","Ramos","Farnandez"]
print(playlist)
print("Length of Playlist :",len(playlist))
playlist.remove("Mbappe")
print(playlist)
print("Length of Playlist :",len(playlist))
print("")

#Remove specified index
#The pop() method removes the specified index
playlist.pop(3)
print(playlist)
print("Length of Playlist :",len(playlist))

#If you do not specify the index, the pop() method remoes the last item
playlist.pop()
print(playlist)
print("Length of Playlist :",len(playlist))
print("")

#The del keyword remoes the specified index:
del playlist[6]
print(playlist)
print("Length of Playlist :",len(playlist))

# #the del keyword can also delete the list completely
# del playlist
# print(playlist)
print("")

#Clear the list
"""The clear() method empties the list.
the list still remains ,but it has no content"""
playlist.clear()
print(playlist)
print("Length of Playlist :",len(playlist))
