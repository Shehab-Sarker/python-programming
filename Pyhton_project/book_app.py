Contact={}

def Showfunction():
    Contact.items()
    print("\nNmae \t Contact")
    for key in Contact:
        print("{} \t {}".format(key,Contact.get(key)))
        
         
while True:
    choice=int(input("1. Add new Contact.\n"
                 "2. Search the contact.\n"
                 "3. Display the Contact.\n"
                 "4. Edit the Contact.\n"
                 "5. Delete the Contact.\n"
                 "6. Exit.\n "
                 "Please write the number between 1-6 : "))
    
    if choice ==1:
        name=input("Add your Contact Name: ")
        phone=input("Add Your phone number: ")
        Contact[name]=phone
    elif choice==2:
        ContactName=input("Serach the contact : ")    
        if ContactName in Contact:
            print(ContactName,"Contact number is ",Contact[ContactName])
        else:
            print(" Not found the Contact.")   
    elif choice == 3:
        if not Contact:
            print("Contact book is empty.")
        else:
            Showfunction()  
    elif choice==4:
        EditContact = input("Edit Your Contact: ")
        if EditContact in Contact:
            phone = input("Change Your Number: ")
            Contact[EditContact]=phone
            print("Contact Updated Successfully.")
        else:
            print("Name is not Found")
    elif choice==5:
        Del_Contact = input("Which Contact do you want to delete? ")
        if Del_Contact in Contact:
            DeletedConfirm=input("Do you want to delete this contact (Y/N)? ")
            if DeletedConfirm =="y" or DeletedConfirm=='Y':  
                Contact.pop(Del_Contact)
            Showfunction()
        else:
            print("The name is not found in the contact")
    else:
        break        
                          
                        
            
                       
        
    
    
    
    