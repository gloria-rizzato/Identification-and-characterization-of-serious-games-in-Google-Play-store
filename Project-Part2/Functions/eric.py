def eric(url):
    from bs4 import BeautifulSoup, SoupStrainer
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    #print(soup.prettify())
    a = soup.find("div", {"class": "abstract"})
    return(a.getText())
        #print(a.getText())
