import json
with open(r"C:\Step IT\StepIT Py\37_pokemon.json", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

print("1)", data["count"])


print("2)", len(data["results"]))


print("3)", data["results"][15])
print(data["results"][15])



print("4)")
for p in data["results"][100:122]:
    print(p["name"])


print("5)")
for p in data["results"]:
    if 'y' in p["name"]:
        print(p["name"])