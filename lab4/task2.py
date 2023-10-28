import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        headers = next(csv_data)
        data = []
        for row in csv_data:
            data.append(dict(zip(headers, row)))

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
