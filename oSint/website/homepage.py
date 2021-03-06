import json
from os import path
import time

import validators
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request
from flask.helpers import url_for
from oSint.scripts.ashok.ashok_script import ashok
from oSint.scripts.cookies.cookiiies import get_cookies, scrape_cookies, start_browser
from oSint.scripts.dns_records import find_ip, get_dns_record
from oSint.scripts.host_discovery_nmap import run_host_discovery
from oSint.scripts.wafw00f.wafw00f import run_wafw00f
from oSint.scripts.ripe_db import get_ripe_info

from oSint.scripts.cookies.sitemap import scrape_sitemap
from oSint.scripts.wappalyzer.wappalyzer import analyze_webpage
from oSint.website.util.session import Session

homepage = Blueprint('homepage', __name__)

browser = None


@homepage.route('/', methods=['GET', 'POST'])
def hompage():
    if request.method == 'POST':

        url = request.form.get('url')
        options = request.form.getlist('hacking-options') if request.form.getlist('hacking-options') else []

        # Check if url is valid
        if not validators.url(url):
            flash("Website not valid.", category='error')
            return render_template("home.html")

        base_url = refactor_url(url)
        Session.set('url', base_url)

        if 'phase-one' in options:
            phase_one(base_url, request.form.getlist('phase-one-options'))
        if 'phase-two' in options:
            phase_two(base_url, request.form.getlist('phase-two-options'))
        if 'phase-three' in options:
            phase_three(base_url, request.form.getlist('phase-three-options'))
        if 'phase-four' in options:
            return phase_four(base_url, request.form.getlist('phase-four-options'))

        print(find_ip(base_url))

        return redirect(url_for('dashboard.overview'))

    Session.reset()
    return render_template("home.html")


def phase_one(url, options):
    ip = find_ip(url)
    print("Phase 1 started")
    options = options if options else []

    if 'nmap' in options:
        print("Running nmap: ", ip)
        hosts = run_host_discovery(ip)
        Session.set('nmap_hosts', hosts)

    if 'ashok' in options:
        print("Running ashok")
        result = ashok(url)
        Session.set('ashok_results', result)

    if 'ripe' in options:
        ip = find_ip(url)
        print("Running RIPE")
        result = get_ripe_info(ip)
        Session.set('ripe_results', result)

def phase_two(url, options):
    print("Phase 2 started")
    options = options if options else []
    if 'wappalyzer' in options:
        print("Running wappalyzer")
        web_technologies = analyze_webpage(url)
        Session.set('web_technologies', web_technologies)


def phase_three(url, options):
    print("Phase 3 started")
    options = options if options else []
    if 'waf00f' in options:
        print("Running waf00f")
        result = run_wafw00f(url)
        Session.set('waf00f', result)


def phase_four(url, options):
    print("Phase 4 started")
    options = options if options else []

    urls = []
    if 'sitemap' in options:
        sitemap = scrape_sitemap(url)
        Session.set('sitemap', sitemap)
        urls = [tuple[0] for tuple in sitemap]
    else:
        urls.append(url)

    global browser
    browser = start_browser()

    cookies_before = get_cookies(browser, urls)
    cookies = {
        'cookies_before': cookies_before
    }
    Session.set('cookies', cookies)

    return redirect(url_for('homepage.step_two'))


@homepage.route('/accept-cookies', methods=['GET', 'POST'])
def step_two():
    if request.method == 'POST':

        global browser

        sitemap = Session.get('sitemap')
        if sitemap:
            urls = [tuple[0] for tuple in sitemap]
        else:
            urls = [Session.get('url')]

        cookies_after = get_cookies(browser, urls)

        cookies = Session.get('cookies')
        cookies['cookies_after'] = cookies_after

        Session.set('cookies', cookies)

        browser.close()

        return redirect(url_for('dashboard.overview'))

    return render_template("accept-cookies.html")


def refactor_url(url):
    return '/'.join(url.split('/')[:3])
