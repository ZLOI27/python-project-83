from random import randint

from page_analyzer.db import get_cursor


class UrlRepository():
    @staticmethod
    def get_all_urls():
        query = """
        SELECT DISTINCT ON (u.id)
            u.id,
            u.name,
            c.created_at AS last_check,
            c.response_status AS last_status
        FROM urls AS u
        LEFT JOIN url_checks AS c ON
            u.id = c.url_id
        ORDER BY u.id, c.created_at DESC
        """
        with get_cursor() as cur:
            cur.execute(query)
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
    def find_by_url(url):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls WHERE name = %s", (url,))
            return cur.fetchone()
    
    @staticmethod
    def get_url(id):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM urls WHERE id = %s", (id,))
            return cur.fetchone()


class UrlCheckRepository():
    @staticmethod
    def get_checks_by_url_id(url_id):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM url_checks WHERE url_id = %s", (url_id,))
            return cur.fetchall()


    @staticmethod
    def add_check(url_id):
        with get_cursor() as cur:
            response_status = randint(400, 420)
            query = """
            INSERT INTO url_checks (
                url_id, 
                response_status, 
                h1, 
                title, 
                description
            ) 
            VALUES (
                %s,
                %s,
                'test-h1',
                'test-title',
                'test-decription'
            )
            """
            cur.execute(query, (url_id, response_status))
            return True