from flask import make_response, jsonify


def check_for_user_key_error(resp):
    """
    Args:
        resp - [description]
    """
    if isinstance(resp, KeyError):
            return 'user with email ' + str(resp) + ' does not exist'


def auth_success_response(message, token, status, status_code):
    return make_response(jsonify({
        'message': message,
        'status': status,
        'token': token.decode('utf-8')
    })), status_code


def response_for_get_all_users(users, status_code):
    return make_response(jsonify({
        'status': 'success',
        'users': users
    })), status_code


def response(message, status, status_code):
    return make_response(jsonify({
        "message": message,
        "status": status
    })), status_code


def convert_list_to_json(lsty):
    """
    converts a list to json
    Args:
        lst - list of objects
    """

    lst = []
    for l in lsty:
        lst.append(l.jsonify())
    return lst
