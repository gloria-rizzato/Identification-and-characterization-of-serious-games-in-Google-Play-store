def app_id(app_name):
    from googlesearch import search
    import re
    query = app_name + 'play store'
    identifier = re.compile('play.google.com')
    id_app_list = []
    for page in search(query, num_results=20, lang='en'):
        if identifier.search(page):
            regex_app_id = '.+\\bdetails\\?id=([^&]+)'
            id_app_list += re.findall(regex_app_id, page)
            break
    id_app = ' '.join(id_app_list)
    return id_app




