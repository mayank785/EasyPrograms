""" Please make sure u name the folder as Little Boy - Hackathon """

with open("../Little Boy - Hackathon/writeup.csv", 'a') as f:
    while True:
        e = input("Enter the txt : ").lower()
        a = input("Answer : ").lower()
        if e == "e":
            break

        f.write(f"{e}, {a}\n")