from app_csv import get_apps
from skim_music import if_serious_music
import google_play_scraper
import urllib.request
from urllib.error import HTTPError
import http.client
import json
from mytinydb import db

res = []
id_nofound = []

path = 'C:/Users/Public/Google-Playstore.csv'
selected_apps = get_apps(path)
id_selected_apps = selected_apps['App Id']

for application in id_selected_apps:
    try:
        result = if_serious_music(application)
        if result is not None:
            res.append(result)
    except urllib.error.HTTPError:
        continue
    except google_play_scraper.exceptions.NotFoundError:
        try:
            id_nofound.append(application)
        except google_play_scraper.exceptions.NotFoundError:
            continue
    except google_play_scraper.exceptions.ExtraHTTPError:
        continue
    except http.client.InvalidURL:
        continue
    except urllib.error.URLError:
        continue
for item in res:
    db.insert(item)

with open('nofound_music', 'w') as fout:
   json.dump(id_nofound, fout)