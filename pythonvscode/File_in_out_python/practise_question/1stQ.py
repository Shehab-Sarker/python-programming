with open("practise.txt","r") as f:
    # f.write("Hi everyone\nwe wre learning File I/0\n")
    # f.write("using Java.\nI like programming in Java")
    data=f.read()
    print(data)

print('')    
new_data=data.replace("Java","Python") 
print(new_data)  
print('')

with open("practise.txt","w") as f:
    f.write(new_data)


word="learning"
# with open("practise.txt","r") as f:
#     data1=f.read()
#     if(data1.find(word)!=-1):
#         print("Word found")
#     else:
#         print("Word not found") 
# if(data.find(word)!=-1):
#     print("word found")
# else:
#     print("Word not found")  

def check_for_word():
    with open("practise.txt","r") as f:
        data1=f.read()
        if(data1.find(word)!=-1):
            print("Word found")
        else:
            print("Word not found")  
            
check_for_word()               