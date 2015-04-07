from django_view_dispatch import dispatch


def get(request):
    return "get", request


class RequestMock():
    def __init__(self, method):
        self.method = method

get_request = RequestMock(method="get")
GET_request = RequestMock(method="GET")


def test_base():
    assert dispatch(get=get)(get_request) == ("get", get_request)


def test_case():
    assert dispatch(get=get)(GET_request) == ("get", GET_request)
    assert dispatch(GET=get)(GET_request) == ("get", GET_request)
    assert dispatch(GET=get)(get_request) == ("get", get_request)
