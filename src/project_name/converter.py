import functools
from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('converter', __name__, url_prefix='/')


def convert_key(elem):
    id = ""
    isId = False
    classes = []
    isClass = False
    tclass = ""
    name = ""
    for c in elem:
        if c == ".":
            if len(tclass) > 0:
                classes.append(tclass)
                tclass = ""
            isClass = True
            isId = False
            continue

        if c == "#":
            if len(tclass) > 0:
                classes.append(tclass)
                tclass = ""
            isId = True
            isClass = False
            continue

        if not isId and not isClass:
            name += c
        elif isId:
            id += c
        elif isClass:
            tclass += c

    if len(tclass) > 0 and isClass:
        classes.append(tclass)
    print(classes)
    return name, id, classes


def convert_elem(elem):
    result = ""
    if isinstance(elem, list):
        result += "<ul>"
        for item in elem:
            result += "<li>"
            result += convert_elem(item)
            result += "</li>"
        result += "</ul>"
    elif isinstance(elem, dict):
        for key in elem.keys():
            name, id, classes = convert_key(key)

            text_class = ""
            for i, cl in enumerate(classes):
                text_class += cl
                if i < len(classes) - 1:
                    text_class += " "

            result += "<" + name + (" id=\"" + id + "\"" if len(id) > 0 else "") +\
                      (" class=\""+text_class+"\"" if len(text_class) > 0 else "") + ">"
            result += convert_elem(elem.get(key, ''))
            result += "</"+name+">"
    else:
        result += elem
    return result


@bp.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    return convert_elem(data)
