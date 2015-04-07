def dispatch(**verbs):
    def dispatch_request(request):
        return verbs["get"](verbs["get"])

    return dispatch_request
