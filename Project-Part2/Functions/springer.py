def springer(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    #print(soup.prettify())
    try:
        a = soup.find("section", id="Abs1")
        if a is not None: #sometimes this method doesn't work
            text = a.find_all('p')
            text_2 = ''
            for i in text:
                text_2 = text_2 + (i.getText()) + '; '
            return(text_2)
            #print(text_2)
        else:
            for tag in soup.find_all("meta"):
                id = tag.get("id", None)
                if (tag.get("property", None) == "og:description"):
                    return (tag.get("content"))
                    #print(tag.get("content"))
    except:
        Exception