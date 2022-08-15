#hello world
import hashlib    #for adding hash to the text or file
import colorama
from hashlib import *    #for finding all hashing 
colorama.init(autoreset=True)
print("""\033[31m

╦ ╦╔═╗╔═╗╦ ╦╦╔╗╔╔═╗  ╔╦╗╔═╗╔═╗╦                                                  
╠═╣╠═╣╚═╗╠═╣║║║║║ ╦   ║ ║ ║║ ║║  
╩ ╩╩ ╩╚═╝╩ ╩╩╝╚╝╚═╝   ╩ ╚═╝╚═╝╩═╝                          
        ,--,
  _ ___/ /\|
 ;( )__, )
; //   '--;
  \     |                  
   ^    ^
""")
print("==============================================")
print("\033[33m11]Hash check\n2]Hash length\n3]Hash type\n4]MD5 Encrypt\n5]MD5 Decrypte\033")
print("==============================================")
choose = input("inter number : ")
if choose == '1':
      hash1 = input("enter hash [1] : ")
      hash2 = input("enter hash [2] : ")
      if hash1 == hash2 :
           print("the hash is clean ")
      else:
           print("the hash is virus ")
           
if choose == '2':
      hash1 = input("enter hash : ")
      print("the hash length is: "+str(len(hash1)))
      
if choose == '3':
      hash = input("enter hash : ")
      hash1 = len(hash)
      if hash1 == 32:
           print("the hash is [MD5] ")
      if hash1 == 40:
           print("the hash is [sha1] ")
      if hash1 == 64:
           print("the hash is [sha256] ")

if choose == '4':
      print("this option for text to MD5 ")
      word = input("Enter your text : ")
      md5 = hashlib.md5(word.encode())  #hashlib from the import
      print(md5.hexdigest())  #hexdigest for writeing random secrpt
     
if choose == '5':
      print("this option for decrption")
      hash = input("Entert the hash : ")
      file = input("write file name : ")
      with open(file , mode='r') as f :
            for line in f :
                     line = line.strip()
                     if md5(line.encode()).hexdigest() == hash:  #will find each hash
                             print("[-] password found : "+line)
      
