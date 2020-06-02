'''
__init__.pyは外部からimportされた時実行される
変数やクラス、メソッドを定義でき、パッケージ単位でのinitが行える
'''

from flask import Flask, make_response, jsonify
from .controllers.icon import killme_path

def create_app():

    app = Flask(__name__)
    app.register_blueprint(killme_path)

    return app

app = create_app()