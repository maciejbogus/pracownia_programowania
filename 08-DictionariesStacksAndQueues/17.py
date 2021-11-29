ICAO = {
    "A":"Alfa",
    "B":"Bravo",
    "C":"Charlie",
    "D":"Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":"Golf",
    "H":"Hotel",
    "I":"India",
    "J":"Juliett",
    "K":"Kilo",
    "L":"Lima",
    "M":"Mike",
    "N":"November",
    "O":"Oscar",
    "P":"Papa",
    "Q":"Quebec",
    "R":"Romeo",
    "S":"Sierra",
    "T":"Tango",
    "U":"Uniform",
    "V":"Victor",
    "W":"Whiskey",
    "X":"X-ray",
    "Y":"Yankee",
    "Z":"Zulu",
}

file = open("ICAO.txt", "w").close()
with open("ICAO.txt", "a") as file:
    for key, value in ICAO.items():
        file.write(f"{key} {value}\n")