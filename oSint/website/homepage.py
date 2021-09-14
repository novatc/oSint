from flask import Blueprint, render_template, request
from flask import current_app as app
from os import path
import validators

homepage = Blueprint('homepage', __name__)

@homepage.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        data = {
            'url' : request.form.get('url'),
        }

        valid = validators.url(data['url'])

        results = {
            'url' : data['url'],
            'valid': valid
        }
        # # # # # # #
        # Do stuff! #
        # # # # # # #
        
        return render_template("results.html", results=results)
        

    return render_template("home.html")
    