def dispatch(**verbs):
    def dispatch_request(request):
        default = verbs.get("default", "GET")
        return verbs.get(default, verbs[default.lower()])(request)

    return dispatch_request
