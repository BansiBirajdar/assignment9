'''1.Write a program which accepts file name from user and check whether that file exists in
current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not.'''
import os
import sys
def main():
    try:
        path=sys.argv[1]
        flag=os.path.isfile(path)
        if(flag==True):
            print("given file is exists in current directory")
        else:
            print("given file is not exists in current directory")
    except IndexError as error:
        print("please enter the file name after .py file")
        print("example:")
        print("python assignment9_1.py file_name.extention")
    finally:
        print("thank you")

if __name__=="__main__":
    main()