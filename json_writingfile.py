import json
from pathlib import Path


movies = [
    {"id": 1, "Name": "Terminator", "year":1982},
    {"id": 2, "Name": "Kindergarden Cop", "year":1983},
    {"id": 3, "Name": "Xmen", "year":1990}
]

data = json.dumps(movies)      #dumps are used to write on a json
print(data)

Path("any_name1.json").write_text(data)      # enter path and then name of the json with write

# To read a json file

x = Path("copy.json").read_text()
print(x)
movies_new = json.loads(x)      #loads are used while upacking json - read/edit on a json
print(movies_new[0]["Name"])