import json
Birthday = {
    "Ylli":"3.2.2001",
    "Adi":"10.9.1993",
    "Dimi":"2.5.1998"
}
with open("JSON.json","w") as f:
    json.dump(Birthday,f)