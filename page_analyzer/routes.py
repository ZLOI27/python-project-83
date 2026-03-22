from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from page_analyzer.repositories import UrlCheckRepository as UCR
from page_analyzer.repositories import UrlRepository as UR
from page_analyzer.services import check_url
from page_analyzer.utils import normalize_url, validate_url


def register_routes(app):
    @app.route('/')
    def index():
        return render_template(
            'index.html',
        )

    @app.route('/urls', methods=['GET'])
    def get_urls():
        urls = UR.get_all_urls()
        return render_template(
            'urls.html',
            urls=urls,
        )

    @app.route('/urls', methods=['POST'])
    def add_url():
        url = request.form.get('url', '').strip()

        if not validate_url(url):
            flash(f"'{url}' URL некорректный!", "danger")
            return render_template(
                'index.html',
                url=url,
            ), 422

        url = normalize_url(url)

        if UR.find_by_url(url) is not None:
            flash(f"'{url}' URL уже в базе", "warning")
            return render_template(
                'index.html',
                url=url,
            ), 409
        
        url_id = UR.add_url(url)
        flash("Страница успешно добавлена", "success")
        return redirect(url_for('get_by_id', id=url_id))

    @app.route('/urls/<int:id>', methods=['GET'])
    def get_by_id(id: int):
        url = UR.get_url(id)
        url_checks = UCR.get_checks_by_url_id(id)

        if url:
            return render_template(
                'url.html',
                url=url,
                url_checks=url_checks,
            )

        flash("Не получены данные из БД", "danger")
        return redirect(url_for('index'))

    @app.route('/urls/<int:id>/checks', methods=['POST'])
    def run_check(id):
        url = UR.get_url(id).get('name', None)
        check_data = check_url(url)

        if check_data is not None and UCR.add_check(id, check_data):
            flash("Страница успешно проверена", "success")
            return redirect(url_for('get_by_id', id=id))

        flash("Произошла ошибка при проверке", "danger")
        return redirect(url_for('get_by_id', id=id))
