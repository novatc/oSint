from Wappalyzer import Wappalyzer, WebPage


def analyze_webpage(url):
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    results = wappalyzer.analyze_with_versions_and_categories(webpage)
    return results
