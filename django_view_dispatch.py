from django.http  import HttpResponseNotAllowed
from weirdict.examples import CaseInsensitiveDict


def dispatch(**kwargs):
    if "default" in kwargs:
        default = kwargs["default"].lower() if hasattr(kwargs["default"], "lower") else kwargs["default"]
        del kwargs["default"]
    else:
        default = "get"

    verbs = CaseInsensitiveDict()
    verbs.update(kwargs)

    def dispatch_request(request, *args, **kwargs):
        if request.method.lower() not in verbs:
            if default in verbs:
                view = verbs[default]
            else:
                # sorted is for determinist ordering for testing purpose
                return HttpResponseNotAllowed(sorted(map(lambda x: x.upper(), verbs.keys())))

        else:
            view = verbs[request.method.lower()]

        return view(request, *args, **kwargs)

    return dispatch_request


def dispatch_strict(**kwargs):
    if "default" not in kwargs:
        kwargs["default"] = None

    return dispatch(**kwargs)
