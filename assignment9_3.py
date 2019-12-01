'''Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt'''

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
            f1=open(file_name,'r',encoding = 'utf-8')
            print("Information about file : ",f1)
            print("Contents of Whole file")
            text=f1.read()
            print(text)
            i=input("do you want to copy all content in another then enter y/n=")
            i=i.lower()
            if(i=='y'):
                file_name=input("please enter the file name with extension=")
                if(file_name.endswith('.txt')):
                    f2=open(file_name,'w',encoding = 'utf-8')
                    f2.write(text)
                    print("")
                    f2.close()
                else:
                    print("extension is not correct")
                    print("please enter the right extension like: \"file_name.txt\" ")
                
            f1.close()
        else:
            raise(FileNotFound("given file is not exists in current directory"))
    except FileNotFound as e:
        print(e)
    finally:
        print("Thank You")
if __name__=="__main__":
    main()