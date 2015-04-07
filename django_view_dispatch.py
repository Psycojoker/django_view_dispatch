from weirdict.examples import CaseInsensitiveDict


def dispatch(**kwargs):
    verbs = CaseInsensitiveDict()
    verbs.update(kwargs)

    def dispatch_request(request):
        return verbs["get"](request)

    return dispatch_request
