import json
import os
import sys


with open(os.path.join(sys.path[0], "json/forbes_billionaires_2016.json")) as json_file:

    data = json.loads(json_file.read())
    # print (data)

def forbes():
    """Return the name, net worth, and industry.
    of the oldest billionaire under 80 years old
    AND the youngest billionaire with a valid age.
    """
    oldest = {}
    youngest = {}

    for entry in data:
        age = entry['age']
        if not oldest or (age > oldest['age']) and (age < 80):
            oldest.update(entry)
        if not youngest or (age < youngest['age']) and (age > 0):
            youngest.update(entry)
    return """
Oldest: Name: %s, Net Worth: %d, Industry: %s , Age: %s
Youngest: Name: %s, Net Worth: %d, Industry: %s, Age: %s
""" % (
        oldest['name'], oldest['net_worth (USD)'], oldest['source'], oldest['age'],
        youngest['name'], youngest['net_worth (USD)'], youngest['source'], youngest['age'],
    )

print(forbes())
