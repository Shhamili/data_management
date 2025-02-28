import json

with open("euro2024.json") as file_handler:
    continut = file_handler.read()
    print(type(continut), continut)
    continut_parsat =json.loads(continut)
    print(type(continut_parsat), continut_parsat)
    
with open("euro2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    print(type(continut_parsat), continut_parsat)