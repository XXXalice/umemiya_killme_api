'''
__init__.pyは外部からimportされた時実行される
変数やクラス、メソッドを定義でき、パッケージ単位でのinitが行える
'''

from flask import Flask, make_response, jsonify

def create_app():

    app = Flask(__name__)

    return app

app = create_app()