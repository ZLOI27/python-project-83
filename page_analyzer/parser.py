from bs4 import BeautifulSoup


def get_content(html: str):
    data = {}
    soup = BeautifulSoup(html, 'html.parser')

    data['h1'] = soup.h1.get_text() if soup.h1 else ''
    data['title'] = soup.title.get_text() if soup.title else ''
    description = soup.find('meta', attrs={'name': 'description'})
    data['description'] = description.get('content', '') if description else ''
    return data
