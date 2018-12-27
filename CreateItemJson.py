import os
import json


def models_item_json(item_name, modid, item_type):
    return {
        "parent": f"item/{item_type}",
        "textures": {
            "layer0": f"{modid}:items/{item_name}"
    }
}


def create_file(data, item_name):
    try:
        filename = f"models/item/{item_name}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open (filename, "w+") as f:
            json.dump(data, f, indent=4)
    except:
        print("Somthing went wrong")
        raise
    else:
        print(f"{item_name}.json file created")


def main():
    item_name = input("item name: ")
    modid = input("modid: ")
    item_type = input("item type. Eg - 'generated' or 'handheld': ")
    create_file(models_item_json(item_name, modid, item_type), item_name)


if __name__ == "__main__":
    main()