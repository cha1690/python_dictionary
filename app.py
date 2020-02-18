import json
from difflib import get_close_matches
with open('data.json') as f:
  data = json.load(f)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) >0:
        YN = raw_input("Did you mean %s. Enter Y for yes, N for No " %get_close_matches(w,data.keys())[0])
        if YN == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif YN == "N":
            return "The word doesnt exist"
    else:
        return "The word doesnt exist"

word = raw_input("Enter word: ")

output = translate(word)

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)

