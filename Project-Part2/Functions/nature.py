def nature(url):
    from bs4 import BeautifulSoup
    import requests
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    #print(soup.prettify())
    for tag in soup.find_all("meta"):
        if (tag.get("name", None) == "dc.description"):
            #print(tag.get("content"))
            return (tag.get("content"))