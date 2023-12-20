from flask import Flask
from config import Config



app = Flask(__name__)
app.config.from_object(Config)




from app.routes.root import *  
from app.routes.user import *