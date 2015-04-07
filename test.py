import os

from django.http  import HttpResponseNotAllowed
from django_view_dispatch import dispatch, dispatch_strict

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"


def get(request):
    return "get", request


def post(request):
    return "post", request


class RequestMock():
    def __init__(self, method):
        self.method = method

get_request = RequestMock(method="get")
GET_request = RequestMock(method="GET")
post_request = RequestMock(method="POST")


def test_base():
    assert dispatch(get=get)(get_request) == ("get", get_request)


def test_case():
    assert dispatch(get=get)(GET_request) == ("get", GET_request)
    assert dispatch(GET=get)(GET_request) == ("get", GET_request)
    assert dispatch(GET=get)(get_request) == ("get", get_request)


def test_basic_dispatch():
    dispatcher = dispatch(get=get, post=post)
    assert dispatcher(get_request) == ("get", get_request)
    assert dispatcher(post_request) == ("post", post_request)


def test_unsupported_method():
    dispatcher = dispatch_strict(get=get)
    result = dispatcher(post_request)
    assert isinstance(result, HttpResponseNotAllowed)
    assert ('Allow', 'GET') in result.items()


def test_unsupported_method_several():
    dispatcher = dispatch_strict(get=get, put=get)
    result = dispatcher(post_request)
    assert isinstance(result, HttpResponseNotAllowed)
    assert ('Allow', 'GET, PUT') in result.items()


def test_default():
    assert dispatch(get=get, put=get)(post_request) == ("get", post_request)
