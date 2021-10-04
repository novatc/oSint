from flask import session
import json

class Session:

    @staticmethod
    def set(key, data):
        session[str(key)] = json.dumps(data, sort_keys=True)

    @staticmethod
    def get(key):
        if key in session:
            return json.loads(session[str(key)])
        else: 
            return None

    @staticmethod
    def reset():
        session.clear()
        session['sitemap'] = json.dumps([])
        session['cookies'] = json.dumps({
            'cookies_after': {},
            'cookies_before': {}
        })
        session['web_technologies'] = json.dumps({})