#Hiding message in an image
import cv2
import string
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


text = input("enter the Secret text: ").lower()
shift_key = int(input("enter the shift number: "))
key = input("Enter the Key to edit(security key) : ")

#Encrypting the secrete Massage 

encrypt = ""
for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_key
        new_letter = alphabet[new_position]
        encrypt += new_letter
      else:
         encrypt += letter

#ASCII Character to ASCII Value and vice versa
d = {}
c = {}
for i in range(255):
  d[chr(i)] = i
  c[i] = chr(i)

#reading image using opencv library

f = cv2.imread(r"C:\Users\Karthik\Desktop\Stegno\Dragon Ball Z.jpg")

#Embedding message into an image
k1 = 0
l = len(encrypt)
z = 0
n = 0
m = 0
lnk = len(key)

for i in range(l):
  f[n,m,z] = d[encrypt[i]]^d[key[k1]]
  n = n+1
  m = m+1
  z = (z+1)%3
  k1 =(k1+1) % lnk

cv2.imwrite("Encrypted_img.jpg",f)
os.startfile("Encrypted_img.jpg")
print("Data hiding in image completed sucessfully.")

k1 = 0
l = len(encrypt)
z = 0
n = 0
m = 0

key1 = input("\n\nRe enter key to extract text:")
decrypt = ""

if key == key1:

  for i in range(l):
    decrypt += c[f[n,m,z]^d[key[k1]]]
    n = n+1
    m = m+1
    z = (z+1)%3
    k1 = (k1+1)%lnk

#Decrypting the Embedded massege 
  plain_text = ""
  for letter in decrypt:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position - shift_key 
        new_letter = alphabet[new_position]
        plain_text += new_letter
      else:
         plain_text += letter
  print("The Secret Message is : ",plain_text)
else:
  print("Key doesn't matched.")