from flask import jsonify as flask_jsonify


def jsonify(obj):

    if type(obj) == list:
        return flask_jsonify([values(x) for x in obj])

    else:
        return flask_jsonify(values(obj))


def values(sqlalchemy_result):

    columns = column_values(sqlalchemy_result)
    additional = additional_values(sqlalchemy_result)
    return {**columns, **additional}


def column_values(sqlalchemy_result):

    columns = sqlalchemy_result.__table__.columns
    return {c.name: getattr(sqlalchemy_result, c.name) for c in columns}


def additional_values(sqlalchemy_result):

    output = {}
    for key, value in sqlalchemy_result.__dict__.items():

        if key == '_sa_instance_state':
            continue

        elif isinstance(value, list):
            output[key] = [values(x) for x in value]

        else:
            output[key] = getattr(sqlalchemy_result, key)

    return output
