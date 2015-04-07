from weirdict.examples import CaseInsensitiveDict


def dispatch(**kwargs):
    verbs = CaseInsensitiveDict()
    verbs.update(kwargs)

    def dispatch_request(request):
        return verbs[request.method.lower()](request)

    return dispatch_request
