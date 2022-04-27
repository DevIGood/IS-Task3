import math

#p - 7 
#q - 11
#e - 47
#For encryption - Hello
#For decryption - 28, 16, 44, 44, 42

print("Last used options.")
myfile = open('sometext.txt', 'r')
print(myfile.read())

myfile.close()

#All define
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
e = int(input("Enter a prime number for e: "))

def prime_check(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

if prime_check(p)==False or prime_check(q)==False or prime_check(e):
    print("Some of the entered numbers are not prime.")

n = p * q
r = (p-1) * (q-1)
 
def gcd_e(e,r):
    while(r!=0):
        e,r = r,e%r
    return e

def euclid_alg(e,r):
    for i in range(1,r):
        while(e != 0):
            a,b = r//e,r%e
            if(b != 0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r = e
            e = b
 
def euclid_alg_ext(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = euclid_alg_ext(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
def multi_inverse(e,r):
    gcd,s,_=euclid_alg_ext(e,r)
    if(gcd != 1):
        return None
    else:
        if(s < 0):
            print("s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s % r
 
#All calculations
print("Euclid's Algorithm")
euclid_alg(e,r)


print("Euclid's Extended Algorithm")
d = multi_inverse(e,r)

print("d = ",d)

public = (e,n)
private = (d,n)
print("Private Key is - ",private)
print("Public Key is - ",public)

 
#Encryption
'''ENCRYPTION ALGORITHM.'''
def encrypt(public,n_text):
    e,n=public
    cypher_text=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c = (m ** e)%n
            cypher_text.append(c)
        elif(i.islower()):               
            m = ord(i)-97
            c = (m ** e)%n
            cypher_text.append(c)
        elif(i.isspace()):
            spc = 400
            cypher_text.append(395)
    return cypher_text
     
 
#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(private,text):
    d,n=private
    plaintext=text.split(',')
    x = ''
    m = 0
    for i in plaintext:
        if(i == '395'):
            x += ' '
        else:
            m = (int(i) ** d)%n
            m += 65
            c = chr(m)
            x += c
    return x
 
#Encryption and Decryption
#For decryption, numbers should be seperated by comma ','

#Choose Encrypt or Decrypt and Print
choise = input("Choose:\n1)Encryption\n2)Decrytion\nYour choice:")
if(choise=='1'):
    plaintext = input("Enter plaintext:")
    cypher_text = encrypt(public,plaintext)
    print(f"Encrypted plaintex - {cypher_text}")
elif(choise=='2'):
    cypher_text = input("Enter plaintext:")
    plaintext = decrypt(private,cypher_text)
    print(f"Decrypted plaintex - {plaintext}")
else:
    print("Wrong input.")

# tofile = open("sometext.txt","w")
# tofile.writelines(str(p)+"\n")
# tofile.writelines(str(q)+"\n")
# tofile.writelines(str(e)+"\n")
# tofile.writelines(str(plaintext))
# tofile.writelines(str(cypher_text))
# tofile.close()

tofile = open("sometext.txt","w")
tofile.write(str(p)+str(q)+str(n)+str(e)+str(plaintext)+str(cypher_text))
tofile.close()