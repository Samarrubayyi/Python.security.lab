








import random
import string

 #كود الاكسرسايز 
characters = string.ascii_letters + string.digits + string.punctuation


random_string = ''.join(random.choice(characters) for _ in range(12))


print("Generated Random String:", random_string)







