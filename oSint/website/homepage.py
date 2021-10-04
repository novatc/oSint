import json
from os import path
import time

import validators
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request
from flask.helpers import url_for
from oSint.scripts.cookies.cookiiies import get_cookies, scrape_cookies, start_browser
from oSint.scripts.dns_records import find_ip, get_dns_record
from oSint.scripts.host_discovery_nmap import run_host_discovery

from oSint.scripts.cookies.sitemap import scrape_sitemap
from oSint.scripts.wappalyzer.wappalyzer import analyze_webpage
from oSint.website.util.session import Session

homepage = Blueprint('homepage', __name__)

browser = None
ip = None

@homepage.route('/', methods=['GET', 'POST'])
def step_one():
    if request.method == 'POST':
        
        url = request.form.get('url')

        valid = validators.url(url)
        if valid:

            base_url = refactor_url(url)
            Session.set('url', base_url)
            
            
            
            sitemap = scrape_sitemap(base_url)
            Session.set('sitemap', sitemap)
            cookie_checkbox = request.form.get('cookie_check')
            global browser


            if cookie_checkbox != None:
                print("Cookies check durchführen...")
                browser = start_browser()
                urls = [tuple[0] for tuple in sitemap]
                cookies_before = get_cookies(browser, urls)

                cookies = {
                    'cookies_before' : cookies_before
                }

                Session.set('cookies', cookies)
            base_url = Session.get('url')
            ip = find_ip(base_url)

            # nmap
            nmap_checkbox = request.form.get('nmap_check')
            if nmap_checkbox != None:
                print("Running nmap...")
                hosts = run_host_discovery(ip)
                Session.set('hosts', hosts)

            # dns
            dns_record = get_dns_record(base_url)
            #Session.set('dns_record', dns_record)
            return redirect(url_for('homepage.step_two'))
        
        else:
            flash("Website not valid.", category='error')


    return render_template("home.html")

@homepage.route('/accept-cookies', methods=['GET', 'POST'])
def step_two():
    if request.method == 'POST':

        global browser
        global ip

        sitemap = Session.get('sitemap')
        urls = [tuple[0] for tuple in sitemap]
        cookie_checkbox = request.form.get('cookie_check')
        if cookie_checkbox != None:
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

