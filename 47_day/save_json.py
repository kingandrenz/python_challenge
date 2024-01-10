import json
def save_json(dic:dict):
    """ takes a dictionary and return a json file. """

    file_n = 'save.json'


    with open(file_n, 'w') as file:
        json.dump(names, file)


names = {'name': 'carol', 'sex': 'female', 'age': 55}
save_json(names)
