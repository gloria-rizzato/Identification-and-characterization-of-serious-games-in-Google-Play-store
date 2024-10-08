import numpy as np
from numpy import random
from tinydb import TinyDB
from app_info import info_app
import csv

list_dict = []
list_other_apps = []
row = []
db = TinyDB('C:/Users/Public/other apps.json')

randomic = np.random.randint(len(db)+1, size=20)
for i in randomic:
    app_doc = db.get(doc_id=i)
    if app_doc is not None:
        info = info_app(app_doc['title'])
        if info is not None:
            fields = ['App name', 'Category']
            row.append([app_doc['title'], info[3]])

with open('other.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(row)









