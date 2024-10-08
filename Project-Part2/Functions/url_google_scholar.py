def url_google_scholar(app_doc):
    import urllib
    app_name = app_doc['title']
    in_url = 'https://scholar.google.com/scholar?'
    getVars = {'hl': 'en', 'q': app_name + ' app'}
    url_scholar = in_url + urllib.parse.urlencode(getVars)
    return url_scholar