import random
import string

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
punctuation1 = random.choice(string.punctuation)
punctuation2 = random.choice(string.punctuation)


password = [uppercaseLetter1, uppercaseLetter2, lowercaseLetter1, lowercaseLetter2, digit1, digit2, punctuation1, punctuation2]
password = random.sample(password, len(password))
password = "".join(password)
print(password)
