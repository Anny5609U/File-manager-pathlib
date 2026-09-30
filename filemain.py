
from pathlib import Path #library through which path can be read
import os

def readfileandfolder(): #what all files and folders exist in explorer (left side menu )
    path = Path('') #the current folder you are at, shows that path
    items = list(path.rglob('*')) ##recursive globe, read files recursively at the current path, and provide its items 
    for i, items in enumerate(items): #enumerate = saving index and values separately
        print(f"{i+1} : {items}") #this will give all the existing files and folders
        #i+1 because python index starts from 0, and result should show 1,2,3,4 not from 0.


def createfile():
    try:  #exception handling before hand to avoid any error
        readfileandfolder()
        name = input("please tell your file name:- ")
        p = Path(name) #adding that file in path
        if not p.exists(): #if files doesnt exist then this will run
            with open(p,"w") as fs: #creating a file , with data adding 
                data = input("what you want to write in this file") #input from the user
                fs.write(data) #adding data into the new file
        else: #if files exists then this will run
            print("this file already exists")

        print(F"FILE CREAETED SUCCESSFULLY")

    except Exception as err:
        print(f"An error occured as {err}")
#2-27 HERE FILE CREATION IS DONE

def readfile():
    try:
        readfileandfolder()
        name = input("which file you want to read (write full file name)")
        p= Path(name)  #if name exist then path mil jayega, if not then it will create a path
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data= fs.read()
                print(data)

            print("FILE READED SUCCESSFULLY")
        else:
            print("the file doesnt exist" )

    except Exception as err:
        print(f" An error occured as {err}")
#30-46 HERE READUING A FILE FUNCTION IS DONE

def updatefile():
    try:
        readfileandfolder()
        name = input("which file do you want to update :- ")
        p= Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending(adding) some content in your file")

            res = int(input("tell your response :- "))
            if res == 1: #will only happen if the user wants to change the name
                name2 = input("tell your new file name :- ") #creating new name
                p2 = Path(name2) #creating new path
                p.rename(p2) #changing name of the path, as well as will change file name

            if res == 2:
                with open(p,'w') as fs:  #here path = p only because user chose to overwrite something in the file
                    data = input("tell what you want to write, this will overwrite the data") 
                    fs.write(data) #this will remove the ealier data in the file and add the new data input by the user

            if res == 3:
                with open(p,'a') as fs:
                    data= input("what do you wanna add")
                    fs.write("" + data)
        print("FILE SUCESSFULLY UPDATED")
      

    except Exception as err:
        print(f"An error has occured as {err}")

#48-62 HERE UPDATING FUNCTION IS PERFORMED

def deletefile():
    try:
        readfileandfolder()
        name= input("which file do you want to delete :- ")
        p= Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file removed successfully")

        else:
            print("no such file exists")

    except Exception as err:
        print(f"An error has occured as {err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check= int(input("please tell your response:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()