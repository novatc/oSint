from flask import Blueprint, render_template, request, flash
from flask import current_app as app
from oSint.scripts.cookies.cookiiies import get_cookies
from oSint.scripts.cookies.sitemap import scrape_sitemaps
from os import path
import validators

homepage = Blueprint('homepage', __name__)

@homepage.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        url = request.form.get('url')

        valid = validators.url(url)
        if valid:

            base_url = refactor_url(url)
            sitemaps = scrape_sitemaps(base_url)
            cookies_before, cookies_after = get_cookies(base_url)

            print(sitemaps)

            # # # # # # #
            # Do stuff! #
            # # # # # # #

            results = {
                'url' : base_url,
                'valid': valid,
                'cookies_before' : cookies_before,
                'cookies_after' : cookies_after
            }

            return render_template("results.html", results=results)
        
        else:
            flash("Website not valid.", category='error')
        

    return render_template("home.html")
    

def refactor_url(url):
    return '/'.join(url.split('/')[:3]) 

