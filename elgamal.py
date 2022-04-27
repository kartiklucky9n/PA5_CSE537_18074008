#!/usr/bin/env python3

#some useful libraries
from Crypto.Util.number import inverse
import random
from binascii import hexlify, unhexlify
from tabulate import tabulate

#gcd of two numbers
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

# Generating large random numbers
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key



#encryption is initiated here, returns two encypted messages c1,c2=(g^y, m.s)
def encrypt(m,g,p,h):

  #g^y
  c1 = pow(g,r,p)
  #s*m
  c2 = (m * pow(h, r, p) ) % p
  return c1,c2

#decryption is initiated here
def decrypt(x,c1,c2,p):
  s = pow(c1,x,p)
  dm = (c2 * inverse(s,p)) % p
  return dm



if __name__ == "__main__":
  input_message = input("Enter message to encrypt: ")
  inputbytes = str.encode(input_message)
  
  #M converted to m using reversible mapping function 
  m = int(hexlify(inputbytes), 16)

  #a cyclic group  G of order  p with generator g.
  p=random.randint(pow(10, 20), pow(10, 50)) #p is q
  
  #generator g
  g= gen_key(p)
  
  #private key generated from the cyclic group G
  r= gen_key(p)# Private key for sender
  
  #x chosen random in in range of order p
  x = random.randint(2, p)

  #h is the public key genrated via the chosen g and x 
  #in the cyclic function
  # Shared Secret (h)
  h = pow(g,x,p)
  
  c1, c2 = encrypt(m,g,p,h)
  
  dm = decrypt(x,c1,c2,p)
  
  x = format(dm, 'x')
  
  message = unhexlify(x)
  


  table=[]
  l1=[]
  l1.append("MESSAGE by Bob         :")
  l1.append(input_message)
 
  l2=[]
  l2.append("MESSAGE converted to an int (M) :")
  l2.append(m)
  
  l3=[]
  l3.append("A random Prime number (P)      :")
  l3.append(p)
  
  
  l4=[]
  l4.append("The generator Generator (G)         :")
  l4.append(g)

  l5  = []
  l5.append("Alice's genrated private key (X) :")
  l5.append(x)
  
  l6=[]
  l6.append("Bob's generated private key (R) :")
  l6.append(r)
  
  l7=[]
  l7.append("Shared secret (H)     :")
  l7.append(h)

  l8=[]
  l8.append("Encrypted Message (C1):")
  l8.append(c1)
  
  l9=[]
  l9.append("Encrypted Message (C2):")
  l9.append(c2)

  l10=[]
  l10.append("Decrypted Integer (dm):")
  l10.append(dm)
  
  l11=[]
  l11.append("Decrypted Hex (x)     :")
  l11.append(x)
  
  l12=[]
  l12.append("Decrypted Message     :")
  l12.append(message)

  table.append(l1)
  table.append(l2)
  table.append(l3)
  table.append(l4)
  table.append(l5)
  table.append(l6)
  table.append(l7)
  table.append(l8)
  table.append(l9)
  table.append(l10)
  table.append(l11)
  table.append(l12)


  print(tabulate(table))
  
