import json
import pytest
import src.PReP as PReP
from flask import jsonify
from . import echo
import bs4


@pytest.fixture
def client():

    PReP.app.config['TESTING'] = True
    PReP.app.config['DEBUG'] = True
    PReP.app.config['USE_JSON'] = False
    PReP.app.config['REQUEST_TEMPLATE'] = "q=::param1::"
    PReP.app.config['SITE_NAME']        = "http://localhost:8081/echo"
    PReP.app.testing = True
    client = PReP.app.test_client()

    yield client


@pytest.fixture
def client2():

    PReP.app.config['TESTING'] = True
    PReP.app.config['DEBUG'] = True
    PReP.app.config['USE_JSON'] = True
    PReP.app.config['REQUEST_TEMPLATE'] = '{"q": "::param1::"}'
    PReP.app.config['SITE_NAME']        = "http://localhost:8081/echo"
    PReP.app.testing = True
    client = PReP.app.test_client()

    yield client


# @pytest.fixture
# def client_echo():
#
#     PReP.app.config['TESTING'] = True
#     PReP.app.config['DEBUG'] = True
#     PReP.app.config['REQUEST_TEMPLATE'] = "q=::param1::"
#     PReP.app.config['SITE_NAME']        = "http://0.0.0.0:8080/echo"
#     PReP.app.testing = True
#     client = PReP.app.test_client()
#
#     yield client


def test_proxy_passing_flat_get(client):

    r = client.get('/get', follow_redirects=True)
    data = json.loads(r.data)  # no security needed as it is just an internal echo server, DON'T expose it btw!

    assert r.status_code == 200
    assert data["args"] == {"q": "::param1::"}


def test_proxy_passing_param_get(client):

    r = client.get('/get?param1=test_integration', follow_redirects=True)
    data = json.loads(r.data)  # no security needed as it is just an internal echo server, DON'T expose it btw!

    assert r.status_code == 200
    assert data["args"] == {"q": "test_integration"}


def test_proxy_passing_param_post(client):

    r = client.get('/post?param1=test_integration', follow_redirects=True)
    print(r.data)
    data = json.loads(r.data)  # no security needed as it is just an internal echo server, DON'T expose it btw!

    assert r.status_code == 200
    assert data["data"] == "q=test_integration"

def test_proxy_passing_param_post_json(client2):
    r = client2.get('/post?param1=test_integration2', follow_redirects=True)
    print(r.data)
    data = json.loads(r.data)  # no security needed as it is just an internal echo server, DON'T expose it btw!

    assert r.status_code == 200
    assert data["form"] == {'q': 'test_integration2'}


#
#
# def test_proxy_passing_param_get(client_echo):
#
#     r = client.get('/get?param1=test_integration', follow_redirects=True)
#     # html = bs4.BeautifulSoup(r.data, features="html.parser")
#     # assert "test_integration" in html.title.text
#     assert r.status_code == 200
