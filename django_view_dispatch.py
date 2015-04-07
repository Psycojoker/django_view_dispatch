def dispatch(**verbs):
    def dispatch_request(request):
        return verbs["get"](request)

    return dispatch_request
