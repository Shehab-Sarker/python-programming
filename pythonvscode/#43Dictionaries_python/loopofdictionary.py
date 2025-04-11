myself={
    "Name":"Shehab Sarker",
    "City":"Rangppur",
    "university":"RUET",
    "ROLL":"210346"
}
x=myself.values()
y=myself.keys()
print(y)
print(x)

for x in myself.keys():
    print(x)
    
print("")    

for x in myself.values():
    print(x)

print("")    
#Loop through both keys and values,by using the items() method
for x,y in myself.items():
    print(x,":",y)
        
print("")        
for x in myself:
    print(x)

for it in myself.items():
    print(it)    