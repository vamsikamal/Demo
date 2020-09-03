# Collection of items with key value pairs
d1 = {"name":"SLC", "location":"Hyd"}
print(d1)                # {'name': 'SLC', 'location': 'Hyd'}

print(d1["name"])        # SLC
print(d1.get("name"))    # SLC

# Update existing item
d1["location"] = "Hyderabad"
print(d1)               # {'name': 'SLC', 'location': 'Hyderabad'}

# Add new item
d1["Course"] = "Python"
print(d1)               # {'name': 'SLC', 'location': 'Hyderabad', 'Course': 'Python'}

# Delete
del d1["Course"]
print(d1)

s = d1.pop("name")
print(d1)
print(s)

d2 = {"name":"SLC", "location":"Hyd", "Course":"Python"}
s1 = d2.popitem()
print(d2)
print(s1)

# deletes all items
d2.clear()   # Deletes items
print(d2)
#del d2       # Deletes dictionary
#print(d2)

# Looping example
d3 = {"name":"SLC", "location":"Hyd", "Course":"Python"}

for key in d3:
    print(key, d3[key])

for key in d3.keys():
    print(key, d3[key])

for k,v in d3.items():
    print(k, v)

for key in d3:
    print(key)

for v in d3.values():
    print(v)