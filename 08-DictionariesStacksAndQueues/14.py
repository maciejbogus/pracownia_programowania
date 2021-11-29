import json

with open("film.json") as file_in:
    data = json.load(file_in)

with open("favourite.json", "w") as file_out:
    json.dump(data, file_out, indent=1)