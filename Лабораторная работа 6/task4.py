import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:

    with open(filename, "r", newline=new_line) as f:

        text = [current[:-1].split(delimiter) for current in f]
        con = [dict(zip(text[0], val)) for val in text[1:]]

        return con


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
