from page_analyzer.db import get_cursor


class UrlRepository():
    @staticmethod
    def get_all_urls():
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls;")
            urls = cur.fetchall()
        return urls
    
    @staticmethod
    def add_url(url):
        return

    @staticmethod
    def get_url_by_name(name):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls WHERE name = %s", (name))
            url = cur.fetchone()
        return url
    
    @staticmethod
    def get_url_by_id(id):
        return


class UrlCheckRepository():
    @staticmethod
    def get_checks_by_url_id(url_id):
        return

    @staticmethod
    def add_check(check):
        return