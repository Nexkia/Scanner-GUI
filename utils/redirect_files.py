import json


def get_path(nameFile):
    return "/home/.ihosp/" + nameFile


def loadPersistent(nameFile):
    path_file = "/home/.ihosp/" + nameFile
    with open(path_file) as json_file:
        return openJson(json_file)


def openJson(json_file):
    try:
        out = json.load(json_file)
    except json.decoder.JSONDecodeError:
        out = {}
    return out
