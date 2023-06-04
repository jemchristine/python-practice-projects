import csv

with open("phonebook.csv", "a") as file:

    name = input("name: ")
    number = input("number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number":number})
#    writer = csv.writer(file)
#    writer.writerow([name, number])

#file.close()