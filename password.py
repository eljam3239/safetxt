import string
import random
import functools

alphabets = list(string.ascii_letters)
digits = list(string.digits)
punc = list(string.punctuation)

#print(alphabets, digits, punc)
length = 18

def generate_password():
    pswd = []
    for i in range(6):
        pswd.append(random.choice(alphabets))
        pswd.append(random.choice(digits))
        pswd.append(random.choice(punc))
    random.shuffle(pswd)
    
    password = functools.reduce(lambda x, y: x+y,pswd)
    return password



if __name__ == "__main__":
    x =generate_password()
    print(x)