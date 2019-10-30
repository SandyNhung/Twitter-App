from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import sys
import config
import logging

app = Flask(__name__,
            template_folder='template/dist',
            static_folder='template/dist/static')
application = app
app.secret_key="session_api_secret_key"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

#create the logger handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(message)s')
log_handler = logging.FileHandler('search.log')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)


from tw33t.views import main

class Search(Resource):
    def get(self, name):
        person = main.getTweet(name)
        logger.info('Result from search : %s', person)
        return person

class UserSearch(Resource):
    def get(self, name):
        user_name = main.getUser(name)
        return user_name

#setup api
CORS(app)
api = Api(app)

api.add_resource(Search, '/timeline-search/<name>')
api.add_resource(UserSearch, '/user-search/<name>')
