import functools
from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('converter', __name__, url_prefix='/')


def convert_elem(elem):
    result = ""
    if isinstance(elem, list):
        result += "<ul>"
        for item in elem:
            print(item)
            result += "<li>"
            result += convert_elem(item)
            result += "</li>"
            print(result)
        result += "</ul>"
    elif isinstance(elem, dict):
        for key in elem.keys():
            result += "<"+key+">"
            result += convert_elem(elem.get(key, ''))
            result += "</"+key+">"
    else:
        result += elem
    return result

@bp.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    return convert_elem(data)
