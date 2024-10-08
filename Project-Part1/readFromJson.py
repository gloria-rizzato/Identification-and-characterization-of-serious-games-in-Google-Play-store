import json

with open("db_music.json", "r") as read_file:
    dictMusic = json.load(read_file)
    realDict = dictMusic['_default']
    print(len(realDict))
    for key, value in realDict.items():
        #dbTOT.insert(value)
        print(value)
