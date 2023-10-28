# TODO решите задачу
import json

IN_FILE = "input.json"


def task(file_path) -> float:
    with open(file_path, 'r') as file:
        data = json.load(file)

    product_sum = 0
    for dictionary in data:
        score = dictionary.get("score", 0)
        weight = dictionary.get("weight", 0)
        product_sum += score * weight

    return round(product_sum, 3)


print(task(IN_FILE))