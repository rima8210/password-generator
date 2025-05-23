#python program to create A Random Password Generator
import random
import string
print("Welcome to our Random Password Generator")
def main():

   length=int(input("Eenter the length of password you want:"))
   lowerD=string.ascii_lowercase
   upperD=string.ascii_uppercase 
   digitD =string.digits
   symbolsD=string.punctuation
   combine=lowerD+upperD+symbolsD
   x=random.sample(combine,length)
   password="".join(x)
   print(password)
main()
main()