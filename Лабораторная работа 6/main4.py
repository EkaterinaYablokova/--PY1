import json
from pprint import pprint

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename, "r", encoding="UTF-8") as file:
        lst = list()
        res_dict = dict()
        for row in file.readlines():
            row = row.split(delimiter)
            row.remove(new_line)
            lst.append(row)

        count_col = len(lst[0])
        for i in range(count_col):
            lst_2 = list()
            for j in range(len(lst)):
                lst_2.append(lst[j][i])
            res_dict[lst_2[0]] = lst_2[1:]

    return [res_dict]


pprint(csv_to_list_dict(INPUT_FILE))

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
