import os

from dotenv import load_dotenv
from flask import Flask, g

from page_analyzer.db import pool
from page_analyzer.routes import register_routes

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
register_routes(app)


@app.before_request
def open_connection():
    g.db = pool.get_conn()


@app.teardown_request
def close_connection(exeption=None):
    conn = g.pop('db, None')
    if conn is not None:
        if exeption:
            conn.rollback()
        else:
            conn.commit()
        pool.putconn(conn)
    