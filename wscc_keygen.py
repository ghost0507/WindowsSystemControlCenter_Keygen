#
# * Program: WSCC - Windows System Control Center v4.x
# * Release: Simple Keygen
# * Created with: Python 3.8.x
#

import hashlib, random

def getMD5(inputText):
  return hashlib.md5(inputText.encode('utf-8')).hexdigest().upper()
  
def GenerateRegCode(name : str):
  Charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  S = getMD5(name + 'WSCC41')
  Result = [None] * 35
  for i in range(35):
    Result[i] = Charset[random.randint(0, len(Charset)-1)]
  Result[25] = S[10]
  S = [None] * 32
  k = 0
  for i in range(35):
    if i!= 2 and i!=14 and i!=32:
      S[k] = Result[i]
      k+=1
  S = getMD5("".join(S))
  Result[2] = S[10]
  Result[14] = S[28]
  return "".join(Result)

name = input("Enter registration name: ")
if(name.strip()==""):
  print("-> Name can't be empty!")
else:
  print('Registration Code : ' + GenerateRegCode(name))