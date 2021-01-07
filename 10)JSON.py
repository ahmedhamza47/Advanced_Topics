import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

json_format = json.dumps(person,indent=4,sort_keys=True)
# converts into the json format, sort keys sorts data alphabetically
print(json_format)

# putting the json data in file
with open('person.json','w') as file:
    json.dump(person,file,indent=4,sort_keys=True)
    #  or file.write(json_format)

with open('person.json','r') as file:  # convert json format to dictionary
    name = json.load(file)
    print(name)

