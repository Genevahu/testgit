'''
---变形凯撒加密解密器----
---作者;胡雨帆---
---日期:20/4/21--
---功能介绍-------
    采用凯撒加密原理进行递归调用函数进行加密解密
    输入.txt文件进行加密后删除源文件,同时输出一个.zzz得加密文件,
    解密时输入.zzz文件,输出.txt
------------------
'''

import os

dictionary= "aA0bB1cC2dD3eE4fF5gG6hH7iI8jJ9kK lL,mM.nN?oO/pP;qQ:rR'sS\"tT!uU@vV$wW%xX&yY-zZ="   ##加密字典
Double_dictionary= dictionary * 2                                                               ##延长字典避免无法判断

def Reverse(one_str):
    return one_str[::-1]

def encryption(num,Input_String,Test_Str="",  k=0):
        ln= len(Input_String)
        if(k<ln):
            j=Input_String[k]
            i=dictionary.find(j)
            temporary_String=Double_dictionary[i + num]
            Test_Str= temporary_String + Test_Str
            Input_String = Input_String.replace(Input_String[0], "", 1)
            k=k+1
            return encryption(i,Input_String,Test_Str)
        else:
            print("The encryption result is\n"+Reverse(Test_Str))
            return Reverse(Test_Str)

def decryption(num,Output_String, Test_Str="", k=0):
    ln = len(Output_String)
    if (k<ln-1):
        j = Output_String[k]
        i = dictionary.find(j)
        temporary_String = Double_dictionary[i - num]
        Test_Str = temporary_String + Test_Str
        k = k + 1
        i=dictionary.find(temporary_String)
        Output_String = Output_String.replace(Output_String[0], "", 1)
        return decryption(i,Output_String,Test_Str)
    else:
        print("The encryption result is\n"+Reverse(Test_Str))
        return Reverse(Test_Str)

def Encryption(File_Name,Enkey):
    File = open(File_Name,"r")
    for line in File:
        File.seek(0)
        Input_String=File.read()
        InputEncrypt=encryption(Enkey,Input_String)
    File.close()
    scan=input("you want Encrpty this test? if you choose yes,we will delete the Original Text document (y/n)\n")
    if(scan=="y" or scan=="Y"):
        with open(file='Encryption_'+str(Enkey)+'.zzz', mode='w') as Enfile:
            Enfile.write(InputEncrypt)
            Enfile.close()
            print("Encrpty done\n")
            os.remove(File_Name)
            print("delete done\n")
            print("Remenber the file name is Encryption_(FILE KEY).zzz")
            print("Bye!")
    else:
        print("byebye!")
        return 0

def Decryption(File_Name,Dekey):
    File=open(File_Name,"r")
    for line in File:
        File.seek(0)
        Output_String=File.read()
        OutputDecrpty=decryption(Dekey,Output_String)
    File.close()
    scan = input("you want Decrpty this test? (y/n)\n")
    if (scan == "y" or scan == "Y"):
        with open(file='Decryption.txt', mode='w') as Enfile:
            Enfile.write(OutputDecrpty)
            Enfile.close()
            print("Decrpty done")
    else:
        print("byebye!")
        return 0

def Testing(File_Name):
    if(os.path.exists(File_Name)):
        return 1
    else:
        return 0

def main():
    print(" ______     __     ______   __  __     ______     ______        ______   ______     ______     __        ")
    print("/\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \      /\__  _\ /\  __ \   /\  __ \   /\ \       ")
    print("\ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<      \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  ")
    print(" \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\       \ \_\  \ \_____\  \ \_____\  \ \_____\ ")
    print("  \/_____/   \/_/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/        \/_/   \/_____/   \/_____/   \/_____/  with Absinthe\n")
    print("Hello,Welcome to the Encryption or Decryption Program")
    switch = input("Would you like to (e)ncrypt  a file, (d)ecrypt  a file, or  do (n)othing  (enter  e, d,  or n)?\n")
    while(switch!="n" or switch!="N"):
        if(switch=="e" or switch=="E"):
            Enkey=input("What  positive integer  key  would you  like to use for encryption?\n")
            if(Enkey.isdigit ()):
                if(int(Enkey)>78 or int(Enkey)<0 ):
                    print(" ------------------------------")
                    print("||wrong scan,please try again!||")
                    print(" ------------------------------")
                    continue
            else:
                print(" ------------------------------")
                print("||wrong scan,please try again!||")
                print(" ------------------------------")
                continue
            Enkey = int(Enkey)
            File_Name=input("Enter  the text-file name to encrypt\n")
            if(Testing(File_Name)==0):
                print(" --------------------------------------")
                print("||wrong path or name,please try again!||")
                print(" --------------------------------------")
                continue
            Encryption(File_Name,Enkey)
            break
        if(switch=="d" or switch=="D"):
            Dekey=input("What  positive integer  key  would you  like to use for decryption?\n")
            if (Dekey.isdigit()):
                if (int(Dekey) > 78 or int(Dekey) < 0):
                    print(" ------------------------------")
                    print("||wrong scan,please try again!||")
                    print(" ------------------------------")
                    continue
            else:
                print(" ------------------------------")
                print("||wrong scan,please try again!||")
                print(" ------------------------------")
                continue
            Dekey=int(Dekey)
            File_Name = input("Enter  the text-file name to decrypt\n")
            if (Testing(File_Name) == 0):
                print(" --------------------------------------")
                print("||wrong path or name,please try again!||")
                print(" --------------------------------------")
                continue
            Decryption(File_Name, Dekey)
            break
        if (switch == "n" or switch == "N"):
            print("Aha! Goodbye!")
            break
        else:
            print("wrong scan,please try again!\n")
            print("----------------------------")
            switch = input("Would you like to (e)ncrypt  a file, (d)ecrypt  a file, or  e(x)it  (enter  e, d,  or n)?\n")



if __name__ == '__main__':
    main()





#