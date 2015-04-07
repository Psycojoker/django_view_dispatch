from django.http  import HttpResponseNotAllowed
from weirdict.examples import CaseInsensitiveDict


def dispatch(**kwargs):
    verbs = CaseInsensitiveDict()
    verbs.update(kwargs)

    def dispatch_request(request):
        if request.method.lower() not in verbs:
            return HttpResponseNotAllowed(map(lambda x: x.upper(), verbs.keys()))

        return verbs[request.method.lower()](request)

    return dispatch_request
