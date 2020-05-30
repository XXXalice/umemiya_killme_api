from flask import Blueprint
from flask import request, make_response, jsonify
import os
from config import VERSION

KILLME_ROOT_PATH = '/api/killme/'
API_ROOT_PATH = os.path.join(KILLME_ROOT_PATH, VERSION)
# ルーティングを定義
killme_path = Blueprint("killme_path", __name__)

@killme_path.route(os.path.join(API_ROOT_PATH), methods=['GET'])
def index_page():

    resp_body = jsonify({
        "usage": [
            {
                "step1.": "This root path ({root}) \n"\
                          "will be numbered with the icon you want.\n"\
                          "(e.g.) {eg}".format(root = API_ROOT_PATH, eg = os.path.join(API_ROOT_PATH, str(10))),
                "step2.": "If you don't know the number, you can specify 0 to enter random mode."
            }
        ]
    })
    resp = make_response(resp_body)
    return resp
