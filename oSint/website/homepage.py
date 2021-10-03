import json
from os import path
import time

import validators
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request
from flask.helpers import url_for
from oSint.scripts.cookies.cookiiies import get_cookies, scrape_cookies, start_browser

from oSint.scripts.cookies.sitemap import scrape_sitemap
from oSint.scripts.wappalyzer.wappalyzer import analyze_webpage
from oSint.website.util.session import Session

homepage = Blueprint('homepage', __name__)

browser = None

@homepage.route('/', methods=['GET', 'POST'])
def step_one():
    if request.method == 'POST':
        
        url = request.form.get('url')

        valid = validators.url(url)
        if valid:

            base_url = refactor_url(url)
            Session.set('url', base_url)
            #print(find_ip(base_url))

            sitemap = scrape_sitemap(base_url)
            Session.set('sitemap', sitemap)

            global browser 
            browser = start_browser()

            urls = [tuple[0] for tuple in sitemap]
            cookies_before = get_cookies(browser, urls)

            cookies = {
                'cookies_before' : cookies_before
            }
            
            Session.set('cookies', cookies)
            
            return redirect(url_for('homepage.step_two'))
        
        else:
            flash("Website not valid.", category='error')


    return render_template("home.html")

@homepage.route('/accept-cookies', methods=['GET', 'POST'])  
def step_two():
    if request.method == 'POST':

        global browser

        sitemap = Session.get('sitemap')
        urls = [tuple[0] for tuple in sitemap]
        cookies_after = get_cookies(browser, urls)
        
        cookies = Session.get('cookies')
        cookies['cookies_after'] = cookies_after
            
        Session.set('cookies', cookies)

        browser.close()

        web_technologies = analyze_webpage(Session.get('url'))
        Session.set('web_technologies', web_technologies)

        return redirect(url_for('dashboard.overview'))


    return render_template("accept-cookies.html")

def refactor_url(url):
    return '/'.join(url.split('/')[:3]) 

