from flask import Blueprint
from flask import request, make_response, jsonify
import os
from config import VERSION

KILLME_ROOT_PATH = '/api/killme/'
API_ROOT_PATH = os.path.join(KILLME_ROOT_PATH, VERSION)
# ルーティングを定義
killme_path = Blueprint("killme_path", __name__)

@killme_path.route(os.path.join(API_ROOT_PATH), methods=['GET'])
def get_icon():
    pass