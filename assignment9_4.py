'''4.Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt'''
import os
import sys
import filecmp
class FileNotFound(Exception):
    def __init__(self,value):
        self.value=value
def main():
    if(len(sys.argv)<=2):
        print("please enter the file name after .py file")
        print("example:")
        print("python assignment9_4.py file_name1.txt file_name2.txt")
        exit()
    try:
        count1=0
        count2=0
        file_name1=sys.argv[1]
        file_name2=sys.argv[2]
        flag1=os.path.isfile(file_name1)
        flag2=os.path.isfile(file_name1)
        if(flag1==True and flag2==True):
            f1=open(file_name1,'r',encoding = 'utf-8')
            f2=open(file_name2,'r',encoding = 'utf-8')
            '''ans=filecmp.cmp(file_name1,file_name2)
            if(ans==True):
                print("both the files contains is same  ")
                print("checking successfull")
            else:
                print("both the files contains is not same  ")
                print("checking successfull")'''
            
            if(f1.read()==f2.read()):
                print("both the files contains is same  ")
                print("checking successfull")
            else:
                print("both the files contains not same contents ")
                print("checking successfull")
            f1.close()
            f2.close()
        else:
            raise(FileNotFound("given file is not exists in current directory"))
    except FileNotFound as e:
        print(e)
    finally:
        print("Thank You")
if __name__=="__main__":
    main()