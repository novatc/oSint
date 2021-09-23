import json
from os import path


import validators
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, session
from flask.helpers import url_for
from oSint.scripts.cookies.cookiiies import get_cookies, scrape_cookies, start_browser
from oSint.scripts.dns_records import *
from oSint.scripts.cookies.sitemap import scrape_sitemap

homepage = Blueprint('homepage', __name__)

browser = None

@homepage.route('/', methods=['GET', 'POST'])
def step_one():
    if request.method == 'POST':
        
        url = request.form.get('url')

        valid = validators.url(url)
        if valid:

            base_url = refactor_url(url)
            session['url'] = json.dumps(url)
            print(find_ip(base_url))
            print(get_dns_record(base_url))

            sitemap_urls = scrape_sitemap(base_url)
            session['sitemap'] = json.dumps(sitemap_urls)

            global browser 
            browser = start_browser()

            cookies_before = get_cookies(browser, sitemap_urls)

            cookies = {
                'cookies_before' : cookies_before
            }
            
            session['cookies'] = json.dumps(cookies)
            
            return redirect(url_for('homepage.step_two'))
        
        else:
            flash("Website not valid.", category='error')


    return render_template("home.html")

@homepage.route('/accept-cookies', methods=['GET', 'POST'])  
def step_two():
    if request.method == 'POST':

        global browser

        sitemap = json.loads(session['sitemap'])
        cookies_after = get_cookies(browser, sitemap)
        
        cookies = json.loads(session['cookies'])
        cookies['cookies_after'] = cookies_after
            
        session['cookies'] = json.dumps(cookies)

        browser.close()
        return redirect(url_for('dashboard.overview'))


    return render_template("accept-cookies.html")

def refactor_url(url):
    return '/'.join(url.split('/')[:3]) 

