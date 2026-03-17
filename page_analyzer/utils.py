from urllib.parse import urlparse

import validators


def normalize_url(url: str):
    parsed = urlparse(url.strip())
    scheme = parsed.scheme.lower()
    hostname = parsed.hostname.lower()
    return f"{scheme}://{hostname}"


def validate_url(url):
    if validators.url(url) is not True:
        return False
    return True
