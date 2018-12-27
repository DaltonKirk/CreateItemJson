import os

def jsonStart():
    return "{\n"

def jsonEnd(indent):    
    return "\n" + jsonIndent(indent) + "}"

def jsonIndent(amount):
    amount = amount * 4
    return " " * amount

def jsonKeyValue(key, value):
    return "\"" + key + "\"" + ": " + "\"" + value + "\""

def jsonKey(key):
    return "\"" + key + "\"" + ": "
    
print("Create new item Json files")
itemName = input("item name: ")
modid = input("modid: ")
itemType = input("item type. Eg - 'generated' or 'handheld': ")

#Create models item json
filename = "models/item/" + itemName + ".json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open (filename, "w+") as f:
    f.write(jsonStart())
    f.write(jsonIndent(1) + jsonKeyValue("parent", "item/" + itemType) + ",\n")
    f.write(jsonIndent(1) + jsonKey("textures") + jsonStart())
    f.write(jsonIndent(2) + jsonKeyValue("layer0", modid + ":items/" + itemName))
    f.write(jsonEnd(1))
    f.write(jsonEnd(0))
