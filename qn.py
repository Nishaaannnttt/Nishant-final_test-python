print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
phoneDirectory={}  #creating one empty dict

while True:

    print(" 1. Add a record \n 2. Search a record \n 3. Update a record \n 4. Delete a record \n 5. Quit")    

    
    option=int(input("Enter your choice: "))
    
    if option==1:                     #first condition to add number and name
        x=input("Enter name: ")
        y=int(input("Enter your 10-digit phone number: "))
        phoneDirectory.update({x:y})              # updates key value pair as input from user
        print("Record added")
        
        
    elif option==2:
        name=input("Enter name to search: ")
        if name in x:
            
            print("{}:{}".format(name,phoneDirectory[name]))             # prints key value pair without braces and ""
        
            
                
    elif option==3:
        new_name=input("Enter name: ")
        if new_name in x:
            new_num=int(input("Enter the new 10-digit number: "))           # for new number asking 
            
            phoneDirectory[new_name]=new_num                               # updates new num in dict
            
        print("Record updated")
        
    elif option==4:
        if len(phoneDirectory)!=0:                                    # when there is key in dict it works and deletes it 
            del_name=input("Enter name: ")
            if del_name in x:
                del phoneDirectory[del_name]
            print("Record deleted")
        else:
            print("The dictionary is empty")                          # else it prints this
        
    elif option==5:
        break                                                        # breaks the loop
                                                                      
    else:
        print("Wrong option entered")
            
        
        
    
            
        
        
        
        
        
    
    
    
    

