from django_view_dispatch import dispatch

def get(request):
    return "get"


class RequestMock():
    def __init__(self, method):
        self.method = method

get_request = RequestMock(method="get")


def test_base():
    assert dispatch(get)(get_request) == "get"
