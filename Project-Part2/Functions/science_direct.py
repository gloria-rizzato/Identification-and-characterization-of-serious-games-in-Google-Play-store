def science_direct (url):
    from bs4 import BeautifulSoup
    import requests

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    #print(soup.prettify())
    a = soup.find("div", id="abstracts")
    text = a.find_all('p')
    text_2 = ''
    for i in text:
        text_2 = text_2 + (i.getText()) + '; '
    #print(text_2)
    return (text_2)



   