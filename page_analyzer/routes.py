from flask import (
    redirect,
    render_template,
    request,
    url_for,
    flash,
    get_flashed_messages
)

from page_analyzer.repositories import UrlCheckRepository, UrlRepository
from page_analyzer.utils import normalize_url, validate_url


def register_routes(app):
    @app.route('/')
    def index():
        messages = get_flashed_messages(with_categories=True)
        return render_template(
            'index.html',
            messages=messages
        )

    @app.route('/urls', methods=['GET'])
    def get_urls():
        urls = UrlRepository.get_all_urls()
        return render_template(
            'urls.html',
            urls=urls
        )

    @app.route('/urls', methods=['POST'])  # FIXME
    def add_url():
        url = request.form.get('url')
        if not validate_url(url):
            flash("Введенный URL некорректный! Возможно не хватает 'HTTP://'", "danger")
            return redirect(url_for('index'))
        
        url = normalize_url(url)

        return redirect(url_for('get_urls'))
        """return render_template(
            'urls.html'
        )"""

    @app.route('/urls/<int:id>', methods=['GET'])
    def get_by_id(id: int):
        url = UrlRepository.get_by_id(id)
        url_checks = UrlCheckRepository.get_checks_by_url_id(id)
        return render_template(
            'url.html',
            url=url,
            url_checks=url_checks,
        )

