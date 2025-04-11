#string type data type
myname1="my name is "
myname="Sheahb Sarker"
print(myname1+myname)
university="Rajshahi University of Engineering and Technology"
print("My University name is " , university)
print('')

#replace the character
txt="Hello World!"
x=txt.replace("H","J")
print(x)
print('')
#Insert the correct syntex to add a placeholder for the age p
age=36
txt="My name is John, and I am    {}"
print(txt.format(age))
print('')
#Return the string without any whitespace at the beginning or the end in python  
txt = "           Hello World "
stripped_txt = txt.strip()
print(stripped_txt)
