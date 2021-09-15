import json
from os import path

import validators
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, session
from flask.helpers import url_for
from oSint.scripts.cookies.cookiiies import get_cookies, scrape_cookies
from oSint.scripts.cookies.sitemap import scrape_sitemap

homepage = Blueprint('homepage', __name__)

@homepage.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        url = request.form.get('url')

        valid = validators.url(url)
        if valid:

            base_url = refactor_url(url)
            urls = scrape_sitemap(base_url)
            cookies_before, cookies_after = scrape_cookies(base_url, urls)
            

            # # # # # # #
            # Do stuff! #
            # # # # # # #

            results = {
                'url' : base_url,
                'cookies_before' : cookies_before,
                'cookies_after' : cookies_after
            }
            session['data'] = json.dumps(results)
            return redirect(url_for('dashboard.overview'))
        
        else:
            flash("Website not valid.", category='error')


    return render_template("home.html")
    

def refactor_url(url):
    return '/'.join(url.split('/')[:3]) 

