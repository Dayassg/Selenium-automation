import csv

#To read a csv file

with open("daya.csv", "r") as Docs:
    reader = csv.reader(Docs)
    check = 0
    for row in reader:
        if row[1] == "Name":
            row[1] = "Masters"
            check = row[1]
            print(check)

print(check)


# To write inside a csv file
with open("daya.csv", "w") as Docs:
    writer = csv.writer(Docs)
    writer.writerow( ["Id","Name","Occupation"])
    writer.writerow(["1", "Dayalan", "QA"])
    writer.writerow(["2", "Suruliappan", "Engineer"])

