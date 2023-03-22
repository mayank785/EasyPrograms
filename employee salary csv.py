import csv

with open("employee.csv") as f:
    csvreader = csv.reader(f, delimiter = ",")
    c = 0
    s = 0
    print("EMPNO\t\tEMPNAME\t\tSALARY")
    print("===============================")
    for rec in csvreader:
        print(f"{rec[0]}\t\t{rec[1]}\t\t{rec[2]}")
        s += int(rec[2])
        if int(rec[2]) > 5000:
            c += 1
    print("===============================")
    print(f"Sum of salary of all the employees : {s}")
    print(f"Employees with salary more than 5000 : {c}")
    print("===============================")

