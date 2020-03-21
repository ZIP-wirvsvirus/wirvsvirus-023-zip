import base64
import copy
import json
import math
import multiprocessing
import traceback
import os

from sqlalchemy import and_, asc
from werkzeug.exceptions import HTTPException
from flask import jsonify, request, Blueprint, current_app, copy_current_request_context, make_response

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
    return jsonify({'success': False, 'msg': text}), code


@endpoint.route('/api/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        r_method = request.json
    else:
        r_method = request.args

    source = r_method.get('source', default=None)

    created_min = r_method.get('created_min', default=None)
    created_max = r_method.get('created_max', default=None)
    update_min = r_method.get('update_max', default=None)
    update_max = r_method.get('update_max', default=None)
    content = r_method.get('content', default=None)
    area = r_method.get('area', default=None)
    category = r_method.get('category', default=None)
    tags = r_method.get('tags', default=None)  # TODO: comma seperated list of regex?
    res = db.session.query(NewsEntry).filter(
        and_(NewsEntry.created.between(created_min, created_max), NewsEntry.created.between(update_min, update_max),
             NewsEntry.content.contains(content), NewsEntry.category.contains(category),
             NewsEntry.source.contains(source), NewsEntry.area.contains(area), NewsEntry.tags.contains(tags))).order_by(
        asc(NewsEntry.id)).all()
    return jsonify(res)
