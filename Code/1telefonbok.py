import collections

d = collections.defaultdict(list)

d["lin"].append("07080103")
d["marcus"].append("070856565")

d["lin"].append("666666")

def printDict():
    print(d)

def AddPerson(name, phonenumber):
    d[name].append(phonenumber)

def UpdatePerson(name):
    numberList = d[name]

    print("which do you want to update?")
    for x, value in enumerate(numberList):
        print("[",x,"]", value)
    recivedInput = int(input())

    d[name][recivedInput] = input("What is the new phone number?")

def DeletePhoneNumber(name):
    numberList = d[name]

    print("which do you want to delete?")
    for x, value in enumerate(numberList):
        print("[",x,"]", value)
    recivedInput = int(input())

    d[name].pop(recivedInput)

def DeletePerson(name):
    d.pop(name)

def AskQuestion():
    print("[1] Lägg till ny person samt telefonnummer")
    print("[2] Uppdatera befintlig persons telefonnummer")
    print("[3] Radera ett persons telefonnummer.")
    print("[4] Radera en person samt alla hens telefonnummer.")
    print("[5] Avsluta programmet")
    print("[6] Skriv ut alla personer")

while True:
    AskQuestion()

    recivedInput = input()

    if recivedInput == "1":
        namn = input("namn: ")
        number = input("nummer: ")
        AddPerson(name=namn, phonenumber=number)
    elif recivedInput == "2":
        namn = input("namn: ")
        UpdatePerson(name=namn)
    elif recivedInput == "3":
        namn = input("namn: ")
        DeletePhoneNumber(name=namn)
    elif recivedInput == "4":
        namn = input("namn: ")
        DeletePerson(name=namn)
    elif recivedInput == "5":
        break
    elif recivedInput == "6":
        printDict()

