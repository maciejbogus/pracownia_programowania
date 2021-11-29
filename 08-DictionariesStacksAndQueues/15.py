import json

student = {
    "imie" : "Maciej",
    "nazwisko" : "Bogus",
    "wiek" : 20,
    "kierunek" : "Informatyka stosowana",
    "uczen_aktywny" : True
}

with open("uczen.json", "w+") as file:
    json.dump(student, file, indent=1)