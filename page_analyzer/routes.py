from flask import render_template
from page_analyzer.models import UrlCheckRepository, UrlRepository


def register_routes(app):
    @app.route('/')
    def index():
        return render_template(
            'index.html'
        )

    @app.route('/urls', methods=['GET'])
    def get_urls():
        all_urls = UrlRepository.get_all_urls()
        return render_template(
            'urls.html',
            all_urls=all_urls
        )

    @app.route('/urls', methods=['POST'])  # FIXME
    def add_url():
        return render_template(
            'urls.html'
        )

    @app.route('/urls/<int:id>', methods=['GET'])
    def get_by_id(id: int):
        url = UrlRepository.get_by_id(id)
        url_checks = UrlCheckRepository.get_checks_by_url_id(id)
        return render_template(
            'url.html',
            url=url,
            url_checks=url_checks,
        )

