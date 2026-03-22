import requests

from page_analyzer.parser import get_content


def check_url(url: str):
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
        response_data = get_content(response.text)
        response_data['status_code'] = response.status_code
        return response_data
    except requests.RequestException:
        return None