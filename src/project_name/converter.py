import functools
from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('converter', __name__, url_prefix='/')


@bp.route('/convert', methods=['POST'])
def convert():
    result = ""
    json_data = request.get_json()
    if isinstance(json_data, list):
        for p in json_data:

            result += "<h1>"+p.get('title', '')+"</h1>\n"
            result += "<p>"+p.get('body', '')+"</p>\n"
    return result
