from flask import Blueprint, render_template, send_from_directory

from crawler.CrawlerManager import CrawlerManager
from database.db import db

main_page = Blueprint("main_page", __name__, template_folder="dist/team23zip",
                      static_folder='dist/team23zip')


@main_page.route("/")
def main_index():
    return render_template('index.html'), 200


@main_page.route("/do_crawl")  # TODO this should be done outside this context, best would be different app...
def do_crawl():
    x = CrawlerManager()
    x.crawl_all(db)
    return render_template('index.html'), 200


@main_page.route("/<path:path>.js")
def get_js(path):
    return send_from_directory('dist/team23zip', path + ".js")


@main_page.route("/assets/<path:path>")
def get_assets(path):
    return send_from_directory('dist/team23zip/assets', path)


@main_page.route('/<path:path>')
def fallback(path):
    return render_template('index.html')
