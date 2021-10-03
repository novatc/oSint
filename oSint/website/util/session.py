from flask import session
import json

class Session:

    @staticmethod
    def set(key, data):
        session[str(key)] = json.dumps(data)

    @staticmethod
    def get(key):
        return json.loads(session[str(key)])