import json

def read_json(st: str):
    """ reads a .json file. """
    with open(st, 'r') as fp:
        data = json.load(fp)

    return data

print(read_json('save.json'))
