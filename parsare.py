import json
from pprint import pprint
    
with open("euro2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    # print(type(continut_parsat), continut_parsat)
    
print(continut_parsat.keys())

tara = "Romania"

groups = continut_parsat["groups"]
pprint(continut_parsat["groups"])

for grup in groups:
    pprint(type(grup))
    pprint(grup["teams"])
    for team in grup["teams"]:
        pprint(type(team))
        pprint(team)
        if team["name"] == tara:
            pprint(f"{tara} se afla in grupa {grup["name"]}")
    