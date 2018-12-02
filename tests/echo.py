from flask import Flask, request, jsonify
import time

app = Flask(__name__)


def extract(d):
    return {key: value for (key, value) in d.items()}


# taken from @see https://github.com/whwright/flask-echo-server/blob/master/echo.py
@app.route('/echo', methods=['GET', 'POST'])
def echo():
    status_code = request.args.get('status') or 200
    status_code = int(status_code)

    data = {
        'success': True,
        'status': status_code,
        'time': time.time(),
        'path': request.path,
        'script_root': request.script_root,
        'url': request.url,
        'base_url': request.base_url,
        'url_root': request.url_root,
        'method': request.method,
        'headers': extract(request.headers),
        'data': request.data.decode(encoding='UTF-8'),
        'host': request.host,
        'args': extract(request.args),
        'form': extract(request.form),
        'json': request.json,
        'cookies': extract(request.cookies)
    }

    response = jsonify(data)
    response.status_code = status_code

    return response


if __name__ == '__main__':
    app.run(host='localhost', port=8081)
