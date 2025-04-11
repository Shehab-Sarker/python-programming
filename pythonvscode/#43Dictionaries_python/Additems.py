myself={
    "Name":"Shehab sarker",
    "university":"RUET",
    "coutry":"Bangladesh",
    "city":"Rajshahi"
}
print("before add key:value pairs:",myself)
myself["Age"]=23
print("After Add key:value pairs:",myself)
print('')
#Update Dictionary
"""The update() method will update the dictionary with the items from a given
argument.if the item does not exist,the item will be added"""
myself.update({"Number":"abcdefgh"})
print("Update Dictionary:",myself)
print('')

myself["city"]="gaibansha"
print(myself)