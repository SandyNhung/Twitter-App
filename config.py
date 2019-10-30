
import os
import warnings
# DEBUG has to be to False in a production enrironment for security reasons
DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CONSUMER_KEY = ""
CONSUMER_SECRET= ""
ACCESS_TOKEN= ""
ACCESS_SECRET= ""

if not (CONSUMER_KEY and CONSUMER_SECRET and ACCESS_TOKEN and ACCESS_SECRET):
    raise Warning('Twitter key empty. Please input!')
