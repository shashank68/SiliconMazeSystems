import random
import string


with open("soMuchData", "w") as f:
    for i in range(10**5):
        f.write(''.join(random.choices(string.ascii_uppercase + string.digits + "}{?._", k = random.randint(20, 10 ** 3))))
        f.write('\n')