from page_analyzer.db import get_cursor


class UrlRepository():
    @staticmethod
    def get_all_urls():
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls;")  # FIXME from 2 tables
            urls = cur.fetchall()
        return urls
    
    @staticmethod
    def add_url(url):
        with get_cursor() as cur:
            cur.execute("""
                INSERT INTO urls (name)
                VALUES (%s)
                RETURNING id
                """, (url,))
            id = cur.fetchone()['id']
            return id

    @staticmethod
    def get_url_by_name(name):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls WHERE name = %s", (name,))
            return cur.fetchone()
    
    @staticmethod
    def get_url_by_id(id):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls WHERE id = %s", (id,))
            return cur.fetchone()


class UrlCheckRepository():
    @staticmethod
    def get_checks_by_url_id(url_id):
        return

    @staticmethod
    def add_check(check):
        return