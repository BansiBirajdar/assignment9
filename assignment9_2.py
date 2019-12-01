'''Write a program which accept file name from user and open that file and display the contents
of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.'''
import os
import sys
class FileNotFound(Exception):
    def __init__(self,value):
        self.value=value
def main():
    if(len(sys.argv)==1):
        print("please enter the file name after .py file")
        print("example:")
        print("python assignment9_2.py file_name.extention")
        exit()
    try:
        file_name=sys.argv[1]
        flag=os.path.isfile(file_name)
        if(flag==True):
            f=open(file_name,'r',encoding = 'utf-8')
            print("Information about file : ",f)
            print("Contents of Whole file")
            print(f.read())
            print("")
            f.close()
        else:
            raise(FileNotFound("given file is not exists in current directory"))
    except FileNotFound as e:
        print(e)
    finally:
        print("Thank You")
if __name__=="__main__":
    main()