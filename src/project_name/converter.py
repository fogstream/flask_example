import functools
from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('converter', __name__, url_prefix='/')


@bp.route('/convert', methods=['POST'])
def convert():
    result = ""
    data = request.get_json()
    if isinstance(data, list):
        result += "<ul>"
        for p in data:
            result += "<li>"
            for key in p.keys():
                result += "<"+key+">"+p.get(key, '')+"</"+key+">"
            result += "</li>\n"
        result += "</ul>"
    else:
        for key in data:
            result += "<" + key + ">" + data.get(key, '') + "</" + key + ">"
    return result
