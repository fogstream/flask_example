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
            for key in p.keys():
                result += "<"+key+">"+p.get(key, '')+"</"+key+">"
            result += "\n"
    return result
