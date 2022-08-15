import random

while True:
    passlen = int(input("Enter the length of password : "))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ."
    p = " ".join(random.sample(s, passlen))
    print(p)
