import json

from typing import Dict, AnyStr
from flask import Flask, request, jsonify
from requests import get, post


app = Flask(__name__)


def tokenize(template: AnyStr, tokens: Dict) -> AnyStr:
    result = template

    for token_name in tokens:
        result = result.replace("::{}::".format(token_name), tokens[token_name])

    return result


@app.route('/get', methods=['GET'])
def proxy_get():
    site_name = app.config['SITE_NAME']
    template  = app.config['REQUEST_TEMPLATE']
    tokenized = tokenize(template, dict(request.args))

    return get(f'{site_name}?{tokenized}').content


@app.route('/post', methods=['GET'])
def proxy_post():
    site_name = app.config['SITE_NAME']
    template  = app.config['REQUEST_TEMPLATE']
    tokenized = tokenize(template, dict(request.args))
    if app.config['USE_JSON']:
        tokenized = json.loads(tokenized)
    return post(f'{site_name}', tokenized).content


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
