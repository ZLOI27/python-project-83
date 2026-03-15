import os

from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

pool = SimpleConnectionPool(
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
