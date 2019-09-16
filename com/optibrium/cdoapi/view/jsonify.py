from flask import jsonify as flask_jsonify


def jsonify(obj):

    if type(obj) == list:
        return flask_jsonify([values(x) for x in obj])

    else:
        return flask_jsonify(values(obj))


def values(sqlalchemy_result):
    columns = sqlalchemy_result.__table__.columns
    return {c.name: getattr(sqlalchemy_result, c.name) for c in columns}
