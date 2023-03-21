def grade(per):
    if per > 90:
        return "A"
    elif per < 90 or per >= 80:
        return "B"
    elif per < 80 or per >= 70:
        return "C"
    elif per < 70 or per >= 60:
        return "D"
    elif per < 60 or per >= 40:
        return "E"
    elif per < 40:
        return "RETEST"
    else:
        return "Something went wrong !"

def main():
    n = int(input("Enter the number of subjects : "))
    s = 0
    for i in range(1, n+1):
        marks = int(input("Enter the marks (out of 100): "))
        s += marks
    p = (s / n)
    g = grade(p)
    print(f"Percetage : {p}\nGrades : {g}")

main()
