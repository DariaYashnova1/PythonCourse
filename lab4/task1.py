import json

IN_FILE = "input.json"

def task(file_path) -> float:
    with open(file_path, 'r') as file:
        data = json.load(file)

    product_sum = sum(dictionary.get("score", 0) * dictionary.get("weight", 0) for dictionary in data)

    return round(product_sum, 3)


print(task(IN_FILE))
