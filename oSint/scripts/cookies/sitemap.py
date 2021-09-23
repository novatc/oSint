import requests
from bs4 import BeautifulSoup
import csv


def scrape_sitemap(base_url):
    url = base_url + '/sitemap.xml'
    # TODO check diffrent sitemaps sitemap_index.xml ...
    result = [base_url]
    with requests.Session() as req:
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = [item.text for item in soup.select("loc")]
        with open("data.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Url", "Status Code"])
            for link in links:
                r = req.get(link)
                #print(link, r.status_code)
                writer.writerow([link, r.status_code])
                if link not in result:
                    result.append(link)
                soup = BeautifulSoup(r.content, 'html.parser')
                end = [item.text for item in soup.select("loc")]
                for a in end:
                    r = req.head(a)
                    #print(a, r.status_code)
                    writer.writerow([a, r.status_code])
                    if a not in result:
                        result.append(a)
    return result

def get_cookies(urls: list):
    session = requests.Session()
    print(session.cookies.get_dict())
    for url in urls:
        response = session.get(url)
        print(session.cookies.get_dict())
    
    return session.cookies.get_dict()
