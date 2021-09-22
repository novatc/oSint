import json
from os import path

import validators
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, session

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def overview():
    url = json.loads(session['url'])
    return render_template("dashboard-overview.html", url = url)
    
@dashboard.route('/dns-ip-analysis')
def phase_1():
    return render_template("dashboard-phase1.html")


@dashboard.route('/metadata-check')
def phase_2():
    return render_template("dashboard-phase2.html")

@dashboard.route('/vulnerability-scan')
def phase_3():
    return render_template("dashboard-phase3.html")

@dashboard.route('/cookie-compliance')
def phase_4():
    cookies = json.loads(session['cookies'])
    return render_template("dashboard-phase4.html", cookies_before = cookies['cookies_before'], cookies_after = cookies['cookies_after'])
