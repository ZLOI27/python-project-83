import requests


def check_url(url: str):
    try:
        response = requests.get(url, timeout=0.5)
        response.raise_for_status()
        response_data = {'status_code': response.status_code}
        return response_data
    except requests.RequestException:
        return None