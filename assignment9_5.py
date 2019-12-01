'''Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt Marvellous
Search “Marvellous” in Demo.txt'''
import os
import sys
class FileNotFound(Exception):
    def __init__(self,value):
        self.value=value
def main():
    if(len(sys.argv)<=2):
        print("please enter the file name after .py file and string")
        print("example:")
        print("python assignment9_5.py file_name.exten. string")
        exit()
        
    try:
        count=0
        file_name=sys.argv[1]
        string=sys.argv[2]
        flag=os.path.isfile(file_name)
        if(flag==True):
            f=open(file_name,'r',encoding = 'utf-8')
            for i in f:
                word=i.split()
                for j in word:
                    if(string==j):
                        count+=1
            if(count==0):
                print("given string is not in file")
                exit()
            else:
                print("frequency of that given string from file ",count)
            f.close()
        else:
            raise(FileNotFound("given file is not exists in current directory"))
    except FileNotFound as e:
        print(e)
    finally:
        print("Thank You")
if __name__=="__main__":
    main()