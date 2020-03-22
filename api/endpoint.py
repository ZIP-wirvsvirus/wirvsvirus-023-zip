from datetime import datetime
import traceback
from sqlalchemy import and_, asc
from werkzeug.exceptions import HTTPException
from flask import jsonify, request, Blueprint, send_from_directory

from database.db import db
from database.models import NewsEntry

endpoint = Blueprint("endpoint", __name__, template_folder="templates")


@endpoint.errorhandler(Exception)
def handle_error(ex):
    code = 500
    text = str(request) + "\n"
    text += str(request.json) + "\n"
    text += str(request.args) + "\n"
    text += str(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
    if isinstance(ex, HTTPException):
        code = ex.code
    print(text)
    return jsonify({'success': False, 'msg': text}), code


@endpoint.route('/api/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        r_method = request.json
    else:
        r_method = request.args
    now = datetime.now()
    time_zero = datetime.min
    source = r_method.get('source', default="")
    created_min = r_method.get('created_min', default=time_zero)
    created_max = r_method.get('created_max', default=now)
    update_min = r_method.get('update_max', default=time_zero)
    update_max = r_method.get('update_max', default=now)
    content = r_method.get('content', default="")
    identifier = r_method.get('identifier', default="")
    area = r_method.get('area', default="")
    category = r_method.get('category', default="")
    tags = r_method.get('tags', default="")  # TODO: comma seperated list of regex?
    res = db.session.query(NewsEntry).filter(
        and_(NewsEntry.created >= created_min, NewsEntry.created < created_max, NewsEntry.last_update >= update_min,
             NewsEntry.last_update < update_max,
             NewsEntry.identifier.contains(identifier),
             NewsEntry.category.contains(category),  # TODO  NewsEntry.content['caption'].contains({"caption": content})
             NewsEntry.source.contains(source), NewsEntry.area.contains(area))).order_by(
        # TODO , NewsEntry.tags.contains(tags)
        asc(NewsEntry.news_id)).all()
    return jsonify([NewsEntry.serialize(x) for x in res])
