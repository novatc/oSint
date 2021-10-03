import requests
from bs4 import BeautifulSoup
import csv


def scrape_sitemap(base_url):
    url = base_url + '/sitemap.xml'
    # TODO check diffrent sitemaps sitemap_index.xml ...
    result = []
    with requests.Session() as req:
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = [item.text for item in soup.select("loc")]
        
        for link in links:
            r = req.get(link)
            result.append([link, r.status_code])
            soup = BeautifulSoup(r.content, 'html.parser')
            end = [item.text for item in soup.select("loc")]
            for a in end:
                r = req.head(a)
                result.append([a, r.status_code])
    return result

def get_cookies(urls: list):
    session = requests.Session()
    print(session.cookies.get_dict())
    for url in urls:
        response = session.get(url)
        print(session.cookies.get_dict())
    
    return session.cookies.get_dict()
