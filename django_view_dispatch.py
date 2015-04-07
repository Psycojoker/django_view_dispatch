from django.http  import HttpResponseNotAllowed
from weirdict.examples import CaseInsensitiveDict


def dispatch(**kwargs):
    verbs = CaseInsensitiveDict()
    verbs.update(kwargs)

    def dispatch_request(request):
        if request.method.lower() not in verbs:
            # sorted is for determinist ordering for testing purpose
            return HttpResponseNotAllowed(sorted(map(lambda x: x.upper(), verbs.keys())))

        return verbs[request.method.lower()](request)

    return dispatch_request
