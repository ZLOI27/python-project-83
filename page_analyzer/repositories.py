from page_analyzer.db import get_cursor


class UrlRepository():
    @staticmethod
    def get_all_urls():
        query = """
            SELECT DISTINCT ON (u.id)
                u.id,
                u.name,
                c.created_at AS last_check,
                c.status_code AS last_code
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
        query = """
            INSERT INTO urls (name)
            VALUES (%s)
            RETURNING id
        """
        with get_cursor() as cur:
            cur.execute(query, (url,))
            id = cur.fetchone()['id']
            return id

    @staticmethod
    def find_by_url(url):
        query = """
            SELECT * FROM urls
            WHERE name = %s
        """
        with get_cursor() as cur:
            cur.execute(query, (url,))
            return cur.fetchone()
    
    @staticmethod
    def get_url(id):
        query = """
            SELECT * FROM urls
            WHERE id = %s
        """
        with get_cursor() as cur:
            cur.execute(query, (id,))
            return cur.fetchone()


class UrlCheckRepository():
    @staticmethod
    def get_checks_by_url_id(url_id):
        query = """
            SELECT * FROM url_checks
            WHERE url_id = %s
            ORDER BY created_at DESC
        """
        with get_cursor() as cur:

            cur.execute(query, (url_id,))
            return cur.fetchall()

    @staticmethod
    def add_check(url_id, check_data):
        data = (
            url_id,
            check_data.get('status_code', ''),
            check_data.get('h1', ''),
            check_data.get('title', ''),
            check_data.get('description', ''),
        )
        query = """
        INSERT INTO url_checks (
            url_id, 
            status_code, 
            h1, 
            title, 
            description
        ) 
        VALUES (%s, %s, %s, %s, %s)
        """
        with get_cursor() as cur:
            cur.execute(query, data)
            return True
