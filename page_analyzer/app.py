import os

from dotenv import load_dotenv
from flask import Flask
from page_analyzer.routes import register_routes

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
register_routes(app)
