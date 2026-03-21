from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from page_analyzer.repositories import UrlCheckRepository, UrlRepository
from page_analyzer.utils import normalize_url, validate_url


def register_routes(app):
    @app.route('/')
    def index():
        return render_template(
            'index.html',
        )

    @app.route('/urls', methods=['GET'])
    def get_urls():
        urls = UrlRepository.get_all_urls()
        return render_template(
            'urls.html',
            urls=urls,
        )

    @app.route('/urls', methods=['POST'])
    def add_url():
        url = request.form.get('url')
        valid = validate_url(url)
        if not valid:
            flash("URL некорректный! Возможно не хватает 'http://'", "danger")
            return render_template(
                'index.html',
                url=url,
            ), 422

        if UrlRepository.find_by_url(url) is not None:
            flash("URL уже в базе", "warning")
            return redirect(url_for('index'))
        
        url = normalize_url(url)
        id = UrlRepository.add_url(url)
        flash("Страница успешно добавлена", "success")
        return redirect(url_for('get_by_id', id=id))

    @app.route('/urls/<int:id>', methods=['GET'])
    def get_by_id(id: int):
        url = UrlRepository.get_url(id)
        url_checks = UrlCheckRepository.get_checks_by_url_id(id)

        if url:
            return render_template(
                'url.html',
                url=url,
                url_checks=url_checks,
            )

        flash("Не получены данные из БД", "danger")
        return redirect(url_for('index'))
