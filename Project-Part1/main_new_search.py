from app_csv import get_apps
from skim_music import if_serious_music
import google_play_scraper
import urllib.request
from urllib.error import HTTPError
import http.client
from app_search import app_id
from mytinydb1 import db

app_list = []

path = 'C:/Users/Public/Google-Playstore.csv'
selected_apps = get_apps(path)

with open('nofound_music.txt') as f:
    lines = f.readlines()
lista = lines[0] 
nofound_musicID = eval(lista) 
print(len(nofound_musicID))

nofound_music_name = []
for id in nofound_musicID:
    nf = selected_apps[selected_apps['App Id'] == id]['App Name']
    nf = nf.to_list()
    nofound_music_name += nf

print(len(nofound_music_name))

for application, names in zip(nofound_musicID,nofound_music_name):
    try:
        ID = app_id(names)
        app_id2 = if_serious_music(ID)
        if app_id2 is not None:
            app_list.append(app_id2)
    except google_play_scraper.exceptions.NotFoundError:
        continue
    except urllib.error.HTTPError:
        continue
    except google_play_scraper.exceptions.NotFoundError:
        continue
    except google_play_scraper.exceptions.ExtraHTTPError:
        continue
    except http.client.InvalidURL:
        continue
    except urllib.error.URLError:
        continue

for item in app_list:
    db.insert(item)