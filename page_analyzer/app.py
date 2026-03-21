import os

from dotenv import load_dotenv
from flask import Flask, g

from page_analyzer.db import DATABASE
from page_analyzer.routes import register_routes

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
register_routes(app)


@app.before_request
def open_connection():
    """Within the framework of a single request from the client, 
    if there are several database requests, 
    one connection is used and only cursors are opened.
    One connection per request also guarantees atomicity.
    """
    pool = DATABASE.get_pool()
    g.db = pool.getconn()


@app.teardown_request
def close_connection(exception=None):
    conn = g.pop('db', None)
    if conn is not None:
        if exception:
            conn.rollback()
        else:
            conn.commit()
        DATABASE.get_pool().putconn(conn)
    