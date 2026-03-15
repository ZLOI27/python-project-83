import os
import psycopg2
from psycopg2.pool import SimpleConectionPool
from contexlib import contextmanager


DATABASE_URL = os.getenv('DATABASE_URL')

pool = SimpleConectionPool(
    minconn=1,
    maxconn=8,
    dsn=DATABASE_URL,
)

@contextmanager
def get_cursor():
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        pool.putconn(conn)
