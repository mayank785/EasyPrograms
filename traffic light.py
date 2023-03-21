def trafficLight():
    signal = input("Enter the colour : ")
    if signal.lower() not in ("red", "yellow", "green"):
        print("Invalid input")
    else:
        val = light(signal)
        if val == 0:
            print("Stop life is more important than speed")
        elif val == 1:
            print("Please go slow")
        else:
            print("You may go now")

def light(colour):
    if colour.lower() == "red":
        return 0
    elif colour.lower() == "yellow":
        return 1
    else:
        return 2

trafficLight()
