# def check_for_line():
#     with open("practise.txt","r") as f:
#         data=f.readline()
#         if(data.find("learning")!=-1):
#             print("Found")
#         else:
#             print("Not Found : -1")   
            
# check_for_line()   

word="learning"
def check_for_word():
    with open("practise.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Word found")
        else:
            print("Word not found")  
            


def check_for_line():
    word="programming"
    data=True
    line_no=1
    with open("practise.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1  
            # if(data.find(word)!=-1):
            #     print("Found")
            # else:
            #     print("Not Found")    
    return -1      
             
check_for_line()            