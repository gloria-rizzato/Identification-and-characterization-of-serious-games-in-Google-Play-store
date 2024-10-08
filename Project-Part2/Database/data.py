from tinydb import TinyDB
from app_field import app_field
import json

db = TinyDB('C:/Users/Public/db_TOT.json') # original database
db_interesting_apps_ADHD = TinyDB('interesting apps ADHD.json') # new database containing apps related ADHD
db_interesting_apps_LSD = TinyDB('interesting apps LSD.json') # new database containing apps related to LSD
db_other = TinyDB('other apps.json') # database containing the remaining apps

for i in range(1, len(db)+1):
    app_doc = db.get(doc_id=i)
    if app_doc is not None:
        app_domain = app_field(app_doc)
        if app_domain == 'ADHD':
            field = {'field': 'ADHD'}
            db_interesting_apps_ADHD.insert(app_doc)
        elif app_domain == 'LSD':
            db_interesting_apps_LSD.insert(app_doc)
        elif app_domain == 'other':
            db_other.insert(app_doc)

db_interesting_apps_ADHD.update({'field': 'ADHD'})
db_interesting_apps_LSD.update({'field': 'LSD'})
db_other.update({'field': 'other'})

db_interesting_apps = TinyDB('interesting apps.json') # new database containing apps related to LSD and ADHD
with open('interesting apps LSD.json','r') as f:
    json_LSD = json.load(f)
    json_LSD = json_LSD['_default']
    for key, value in json_LSD.items():
        db_interesting_apps.insert(value)
with open('interesting apps ADHD.json','r') as read_file:
    dictWord = json.load(read_file)
    realDict = dictWord['_default']
    for key, value in realDict.items():
        db_interesting_apps.insert(value)