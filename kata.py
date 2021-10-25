import json
import os
import sys


with open(os.path.join(sys.path[0], "forbes_billionaires_2016.json")) as json_file:

    data = json.load(json_file)

def forbes():
    oldest = {}
    youngest = {}

    for entry in data:
        age = entry['age']
        if not oldest or (age > oldest['age']) and (age < 80):
            oldest.update(entry)
        if not youngest or (age < youngest['age']) and (age > 0):
            youngest.update(entry)

    old_bean = oldest['name'], oldest['net_worth (USD)'], oldest['source'],
    youngen = youngest['name'], youngest['net_worth (USD)'], youngest['source'],

    return old_bean, youngen
print(forbes())
