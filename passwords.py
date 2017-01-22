###############  PYTHON 3 IS REQUIRED FOR THIS APP WORKS #################

# Simple Python code to make a random secure 12 character passwords
# Fell free to change the lenght of passwords
# Enter any name you whant to convert as password



import string
import random
def generator():
    letter1=random.choice(string.ascii_lowercase)
    letter2=random.choice(string.ascii_uppercase)
    letter3=random.choice(string.hexdigits)
    letter4=random.choice(string.punctuation)
    letter5=random.choice(string.digits)
    letter6=random.choice(string.punctuation)
    letter7=random.choice(string.ascii_lowercase)
    letter8=random.choice(string.ascii_uppercase)
    letter9=random.choice(string.hexdigits)
    letter10=random.choice(string.punctuation)
    letter11=random.choice(string.ascii_lowercase)
    letter12=random.choice(string.punctuation)
    name=letter1+letter2+letter3+letter4+letter5+letter6+letter7+letter8+letter9+letter10+letter11+letter12
    return (name)
x = input("enter any name to convert: ")

print("sugested password is {} ".format(generator()))
