
import string
from random import sample

def get_random_password(n=8) -> str:


    password = string.digits + string.ascii_letters
    password_ = "".join(sample(password, n))
    return password_




print(get_random_password())
