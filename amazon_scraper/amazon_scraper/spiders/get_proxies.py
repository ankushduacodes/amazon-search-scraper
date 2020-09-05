import bs4
import requests


url = "https://www.us-proxy.org/"

headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

def get_proxy_set():

    req = requests.get(url, headers=headers)

    proxy_set = set()

    soup = bs4.BeautifulSoup(req.content, "html5lib")

    tr_tags = soup.findAll('tr')

    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all('td')
        try:
            if td_tags[2].text == "US":
                proxy_set.add(td_tags[0].text + ':' + td_tags[1].text)
        except:
            continue
    
    return proxy_set