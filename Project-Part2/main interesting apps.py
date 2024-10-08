from tinydb import TinyDB
from bs4 import BeautifulSoup
import requests, re, csv
from url_google_scholar import url_google_scholar
from eric import eric
from ieee import ieee
from nature import nature
from science_direct import science_direct
from springer import springer
from nlpG import nlp
from scopus import scopus
from study_type import type_study
from app_info import info_app

list_dict = []
list_other_apps = []
list_ADHD_apps = []
list_LSD_apps = []
list_abstracts = []
list_urls = []
list_of_dict = []
list_TYPE = []
abstract = ''
row_ADHD = []
row_LSD = []

regex_site_springer = '(http|https):\/\/link.springer.com\/.*'
regex_site_nature = '(http|https):\/\/www.nature.com\/.*'
regex_site_eric = '(http|https):\/\/eric.ed.gov\/.*'
regex_site_ieee = '(http|https):\/\/ieeexplore.ieee.org\/.*'
regex_site_science = '(http|https):\/\/www.sciencedirect.com\/.*'
regex_site_scopus = '(http|https):\/\/www.scopus.com\/.*'
type_paper = ['observational study', 'randomised control trials', 'systematic review', 'meta analysis']
db = TinyDB('C:/Users/Public/interesting apps.json')
with open('C:/Users/Public/SystematicReview.txt') as f:
    text_sr = f.read()
    words_sr = nlp(text_sr)
with open('C:/Users/Public/MetaAnalysis.txt') as f:
    text_ma = f.read()
    words_ma = nlp(text_ma)
with open('C:/Users/Public/ObservationalStudy.txt') as f:
    text_os = f.read()
    words_os = nlp(text_os)
with open('C:/Users/Public/RCT.txt') as f:
    text_rct = f.read()
    words_rct = nlp(text_rct)
for i in range(1,12):
    app_doc = db.get(doc_id=i)
    app_domain = app_doc['field']
    url_scholar = url_google_scholar(app_doc)
    response = requests.get(url_scholar)
    # print(f'url google scholar: {url_scholar}')
    soup = BeautifulSoup(response.content, 'lxml')
    for item in soup.select('[data-lid]'):
        try:
            urls = item.find_all('h3', {"class": "gs_rt"})[0].a['href']
            for url_paper in urls.split():
                #print(url_paper)
                if re.match(regex_site_springer, url_paper, flags=0) is not None:
                    abstract = springer(url_paper)
                    # print(abstract)
                elif re.match(regex_site_nature, url_paper, flags=0) is not None:
                    abstract = nature(url_paper)
                    # print(abstract)
                elif re.match(regex_site_eric, url_paper, flags=0) is not None:
                    abstract = eric(url_paper)
                    # print(abstract)
                elif re.match(regex_site_ieee, url_paper, flags=0) is not None:
                    abstract = ieee(url_paper)
                    # print(abstract)
                elif re.match(regex_site_science, url_paper, flags=0) is not None:
                    abstract = science_direct(url_paper)
                    # print(abstract)
                elif re.match(regex_site_scopus, url_paper, flags=0) is not None:
                    abstract = scopus(url_paper)
                if len(abstract) > 0:
                    abstract_nlp = nlp(abstract)
                    list_urls.append(url_paper)
                    list_abstracts.append(abstract)
                    common_sr = list(set(abstract_nlp) & set(words_sr))
                    common_os = list(set(abstract_nlp) & set(words_os))
                    common_ma = list(set(abstract_nlp) & set(words_ma))
                    common_rct = list(set(abstract_nlp) & set(words_rct))
                    TYPE = type_study(common_sr, common_os, common_ma, common_rct)
                    list_TYPE.append(TYPE)
                abstract = ''
        except:
            Exception
    info = info_app(app_doc['title'])
    dev = app_doc['developer']
    pri = app_doc['price']
    pri = "{:.2f}".format(pri)
    if pri == '0.00':
        pri = 'Free'
    # order = id, released, score, category
    if info is not None:
        if app_domain == 'ADHD':
            row_ADHD.append([app_doc['title'], dev, info[1], info[2], pri, list_urls, list_TYPE])
            list_urls = []
            list_abstracts = []
            list_TYPE = []
        if app_domain == 'LSD':
            row_LSD.append([app_doc['title'], dev, info[1], info[2], pri, list_urls, list_TYPE])
            list_urls = []
            list_abstracts = []
            list_TYPE = []
    else:
        if app_domain == 'ADHD':
            row_ADHD.append([app_doc['title'], dev, '[]', '[]', pri, list_urls, list_TYPE])
            list_urls = []
            list_abstracts = []
            list_TYPE = []
        if app_domain == 'LSD':
            row_LSD.append([app_doc['title'], dev, '[]', '[]', pri, list_urls, list_TYPE])
            list_urls = []
            list_abstracts = []
            list_TYPE = []
fields = ['App name', 'Developer', 'Release', 'Score', 'Price', "Paper's urls", "Paper's category"]
print(len(row_LSD))
print(len(row_ADHD))
with open('learning_disorders.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(row_LSD)
f.close()
with open('attention deficit.csv', 'w') as n:
    write = csv.writer(n)
    write.writerow(fields)
    write.writerows(row_ADHD)
n.close()