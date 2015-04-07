def dispatch(**verbs):
    def dispatch_request(request):
        return verbs.get("get", verbs.get("GET"))(request)

    return dispatch_request
