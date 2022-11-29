import json

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    with open(filename, 'r') as f:
        values = []
        for line in f:
            words = line.rstrip("\n").split(',')
            values.append(words)
            values = values[::2]
            headers = values[0]
            values = values[1:]

            result = []
            for vals in values:
                vals = [format(float(val), '.6f') for val in vals]
                result.append(dict(zip(headers,vals)))
                return result
    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
