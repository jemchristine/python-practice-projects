#people = dict() - same as below
people = {
    "Carter" : "09",
    "David" : "091"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")